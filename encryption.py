# -*- coding: UTF-8 -*-
import base64

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

from django.conf import settings
from django.core.exceptions import ValidationError


class Cipher:
    """Encryption base class for LicenseKey and DLCKey tables

    Create a new Cipher object: Cipher('product_key')
    """
    secret_key = settings.CIPHER_SECRET_KEY
    block_size = AES.block_size
    hash_secret_key = settings.HASH_SECRET_KEY
    # Don't ever try to change this value
    emergency_state = False

    def __init__(self, object_key):
        self.object_key = object_key

    def encrypt(self):
        raw = self.pad(self.object_key)
        iv = Random.new().read(Cipher.block_size)
        cipher = AES.new(Cipher.secret_key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    @classmethod
    def decrypt(cls, enc):
        enc = base64.b64decode(enc)
        iv = enc[:cls.block_size]
        cipher = AES.new(cls.secret_key, AES.MODE_CBC, iv)
        return cls.unpad(cipher.decrypt(enc[cls.block_size:]))

    def pad(self, s):
        return (s + (Cipher.block_size - len(s) % Cipher.block_size) *
                chr(Cipher.block_size - len(s) % Cipher.block_size))

    @staticmethod
    def unpad(s):
        return s[:-ord(s[len(s) - 1:])]

    def hash_product_key(self, product_id):
        from products.models import Product
        hash_obj = SHA256.new(Cipher.hash_secret_key)
        drm_affix = Product.objects.get(pk=product_id).drm_type.name
        hash_obj.update(drm_affix + self.object_key)
        hash_string = hash_obj.hexdigest()
        return hash_string

    @staticmethod
    def check_hash_uniqueness(hash_product_key):
        from products.models import LicenseKey, DLCKey
        if (LicenseKey.objects.filter(hash_value=hash_product_key).exists() or
                DLCKey.objects.filter(hash_value=hash_product_key).exists()):
            return False
        return True

    # DON'T use this method
    # This method is use, to encrypt every key in the database
    @classmethod
    def _update_db(cls):
        cls.emergency_state = True
        from products.models import LicenseKey, DLCKey
        tables = [LicenseKey, DLCKey]
        for table in tables:
            for row in table.objects.all():
                try:
                    decrypted_value = cls.decrypt(row.value)
                except (ValueError, TypeError):
                    pass
                else:
                    if cls(decrypted_value).hash_product_key(
                            row.product_id) == row.hash_value:
                        # everything is all right, skip
                        continue

                if not row.value:
                    # lack of key, skip
                    print('Lack of key for instance: {0}\n'.format(row))
                elif cls(row.value).hash_product_key(
                        row.product_id) == row.hash_value:
                    # for some reason key isnt encrypt and hash value
                    # is correct, skip
                    print('For some reason key isnt encrypted and hash value'
                          ' is correct')
                    print('Instance: {0}\n'.format(row))
                elif not row.hash_value:
                    if len(row.value) >= 40:
                        input_value = raw_input(
                            'Instance: {0}, key_value={1}\n'
                            'There might be posibility that the key is already'
                            ' encrypted. Do you want to proceed(yes/no)?'.
                            format(row, row.value))
                        if input_value != 'yes':
                            continue
                    # encrypt and generate hash value
                    try:
                        row.clean()
                        row.save()
                    except ValidationError, e:
                        print('Bad instance: {0}'.format(row))
                        print('{0}\n'.format(e))
                else:
                    # show bad instances
                    print('Bad instance: {0}'.format(row))
                    print('Value: {0}, Hash value: {1}\n'.format(
                        row.value, row.hash_value))
        cls.emergency_state = False

    # DON'T use this method
    # This method is use when secret key and hash key were lost
    @classmethod
    def _reverse_encryption_and_clear_hash_values(
            cls, old_secret_key, old_hash_secret_key):
        from products.models import LicenseKey, DLCKey
        cls.secret_key = old_secret_key
        cls.hash_value = old_hash_secret_key
        cls.emergency_state = True
        tables = [LicenseKey, DLCKey]
        for table in tables:
            for row in table.objects.all():
                try:
                    original_key = cls.decrypt(row.value)
                except (ValueError, TypeError):
                    print('Bad instance: {0}'.format(row))
                    print('Value: {0}, Hash value: {1}\n'.format(
                        row.value, row.hash_value))
                    continue
                cipher_instance = cls(original_key)
                if cipher_instance.hash_product_key(
                        row.product_id) == row.hash_value:
                    # reverse encryption
                    row.value = original_key
                    row.hash_value = None
                    row.save()
                else:
                    print('Bad instance: {0}'.format(row))
                    print('Value: {0}, Hash value: {1}\n'.format(
                        row.value, row.hash_value))

        cls.secret_key = settings.CIPHER_SECRET_KEY
        cls.hash_value = settings.HASH_SECRET_KEY
        cls.emergency_state = False



# print(SHA256.new('yukynyu').digest())
# print(os.urandom(16))
# print(hashlib.sha256("awesome").digest())

# print(len(Cipher.decrypt('')))

# c = Cipher('')
# en = c.encrypt()
# # print(len(en))
# # print(len(c.decrypt(en)))
# print(c.hash_product_key(1))


def clean(self):
        if self.pk and not Cipher.emergency_state:
            old_instance = DLCKey.objects.get(pk=self.pk)
            if self.value != old_instance.value:
                raise ValidationError(
                    _("Don't ever try to change key product"))
            if self.hash_value != old_instance.hash_value:
                raise ValidationError(
                    _("Don't ever try to change hash value of the product"))
            if self.product != old_instance.product:
                raise ValidationError(
                    _("Don't ever try to change product for this key"))
        if self.value and not self.hash_value:
            cipher_obj = Cipher(self.value)
            self.value = cipher_obj.encrypt()
            hash_value = cipher_obj.hash_product_key(self.product_id)
            if not cipher_obj.check_hash_uniqueness(hash_value):
                raise ValidationError(
                    _("Duplicated hash_value: {0}, for key/drm_type pair".
                        format(hash_value)))
            self.hash_value = hash_value
        else:
            decrypted_value = Cipher.decrypt(self.value)
            if not (Cipher(decrypted_value).hash_product_key(
                    self.product_id) == self.hash_value):
                raise ValidationError(_("Something went terribly wrong !"))

    def save(self, *args, **kwargs):
        if Cipher.emergency_state:
            print('DANGER!')
            super(DLCKey, self).save(*args, **kwargs)
        else:
            # protection for shell changes in the model
            self.clean()
            super(DLCKey, self).save(*args, **kwargs)

        # if not kwargs.pop('update_status', None) or not Cipher.emergency_state:
        #     # protection for shell changes in the model
        #     self.clean()
        # super(DLCKey, self).save(*args, **kwargs)            
