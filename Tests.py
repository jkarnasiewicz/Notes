from django.test import TestCase, RequestFactory, modify_settings, override_settings

response = self.client.get(reverse('promo_terms_of_use'), {'force_district': 'PL'}, follow=True)

@modify_settings(MIDDLEWARE_CLASSES={
    'append': MIDDLEWARE_CLASSES,
    'prepend': 'django.middleware.cache.UpdateCacheMiddleware',
})

@override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                   CELERY_ALWAYS_EAGER=True,
                   BROKER_BACKEND='memory')

@override_settings(DEBUG=True)

@override_settings(TEMPORARY_UNAVAILABLE=True)
def test_temporary_unavailable(self):
    response = self.client.get('/', follow=True)
    # expected_html = render_to_string('temporary_unavailable.html')
    self.assertIn('We are sorry!', response.content)
    # from django.conf import settings
    # print(settings.TEMPORARY_UNAVAILABLE)
    # print(response.templates)

    # found = resolve('/')
    # self.assertEqual(found.func, home)


print(response.redirect_chain)
print(response.context['form'])
for t in response.templates:
            print(t.name)

print(response.resolver_match.func.__name__)
print(response.resolver_match.func.__module__)


self.client.login(username='john', password='blowfish')
self.client.force_login(self.super_user)
self.client.logout()

response = self.client.get('/admin/product/{0}/change/'.format(product.pk), follow=True)
response = self.client.post('/admin/product/add/', new_coupon_template, follow=True)

self.assertIn('number', response.context['adminform'].form.errors)

self.assertEqual(response.status_code, 200)
self.assertEqual(response.resolver_match.func, my_view)
self.assertTrue(response.context['form'], RedeemForm)
self.assertEqual(response.request['PATH_INFO'], '/admin/coupons/coupontemplate/add/')
self.assertTemplateUsed(response, 'coupons/redeem.html')
self.assertTrue('userena/profile_feed.html' in [temp.name for temp in response.templates])

self.assertRedirects(response, reverse('userena_profile_detail', kwargs={'username': user.username}))
self.assertRedirects(response, '/admin/coupons/coupontemplate/', status_code=302, target_status_code=200)


ORDER save()
ORDER save()
[01/Jun/2016 14:53:02] "POST /payments/getpaid.backends.dummy/payment/authorization/15436/ HTTP/1.1" 302 0
[01/Jun/2016 14:53:02] "GET /payments/payment/success/15436/ HTTP/1.1" 302 0
ORDER save()
[01/Jun/2016 14:53:03] "GET /pl/orders/finished/5c19798c1c3ea7f24399547febb9351048122b67/ HTTP/1.1" 200 9225
[01/Jun/2016 14:53:03] "GET /static/js/ee-transactions.js HTTP/1.1" 200 707
[01/Jun/2016 14:53:04] "GET /static/img/btn_mask_green.png?0207e6b55da4 HTTP/1.1" 200 2324


POST
'csrfmiddlewaretoken=SnYztUdv0WoNBQy6c3v2FYjBmYMU06Rw&=true&order_id=49727&use_wallet=0'
<QueryDict: {u'': [u'true'], u'order_id': [u'49727'], u'csrfmiddlewaretoken': [u'SnYztUdv0WoNBQy6c3v2FYjBmYMU06Rw'], u'use_wallet': [u'0']}>