# General
django-admin.py startproject mysite          # Creating Project "mysite"

python manage.py startapp myapp              # Creating new app named myapp
python manage.py test myapp                  # Run test in myapp application

python manage.py runserver                   # Run development server / python manage.py runserver 8080
python manage.py runserver --settings=settings.production
python manage.py runserver --insecure        # Run in insecure mode and serve static locally (e.g. for testing without debug)


python manage.py syncdb                      # Creating necessary db for settings.py
python manage.py syncdb --database=external_db

python manage.py shell                       # Shell, pip install ipython (improve shell)
#                                            # help('django.forms'), help(ModelForm)

python manage.py sql model_name				 # Sql for model_name class
python manage.py reset model_name			 # reset all the data and update model schema

python manage.py dumpdata --indent=2 > db_backup.json     # Export all data to file db_backup.json
python manage.py dumpdata offers.District --exclude=auth --exclude=contenttypes > db_test.json
python manage.py loaddata db_backup.json

./manage.py inspectdb --database=external_db        # show django models.py for specify databse
./manage.py inspectdb > models.py                   # copy to models.py file

./manage.py test -v3					     # Test whole site with verbosity level 2(0-3)
./manage.py test myapp 						 # Test only myapp
./manage.py test -v3 --keepdb                # Preserving test database
./manage.py test --pattern="tests_*.py"      # Specify custom filename pattern
python -Wall manage.py test                  # The -Wall flag tells Python to display deprecation warnings


./manage.py collectstatic					 # Collect all the static files
./manage.py createpermissions                # Creating new permissions define in xml file
./manage.py createsuperuser

./manage.py update --help					 # Help for additional management command(update)

# Migrations (table with migrated schema tables: django_migrations)
./manage.py makemigrations
./manage.py migrate
./manage.py showmigrations

./manage.py migrate --fake
./manage.py migrate --fake-initial




Django DB
##########################################################################################################

# This will run on the 'default' database.
Author.objects.all()

# So will this.
Author.objects.using('default').all()

# This will run on the 'other' database.
Author.objects.using('other').all()



# To save an object to the legacy_users database
my_object.save(using='legacy_users')
# Working with MySQL DB
apt-get install python-mysqldb
apt-get install build-essential python-dev libmysqlclient-dev
pip install MySQL-python


# Working with MsSQL DB
# http://blog.tryolabs.com/2012/06/25/connecting-sql-server-database-python-under-ubuntu/
sudo apt-get install unixodbc unixodbc-dev freetds-dev tdsodbc
(virtual-env) pip instal pyodbc

# edit the file /etc/freetds/freetds.conf
[sqlserver]
    host = <ip address of the computer running SQL Server>
    port = <port>
    tds version = 7.2

# edit the file /etc/odbcinst.ini
# edit the file /etc/odbc.ini
# and from python PYODBC
import pyodbc
dsn = 'sqlserverdatasource'
user = ''
password = ''
database = ''

con_string = 'DSN={};UID={};PWD={};DATABASE={};'.format(dsn, user, password, database)
cnxn = pyodbc.connect(con_string)
cursor = cnxn.cursor()

cursor.execute("Select id From SpinLab_Stations;")
cursor.fetchall()




South
##########################################################################################################

# Normal Changes
manage.py schemamigration myapp --auto       # manage.py schemamigration southtut --auto --update
manage.py migrate myapp                      # re add initial_data from json


# The First Migration
manage.py schemamigration myapp --initial
manage.py migrate myapp --fake


# Converting Existing Applications
manage.py syncdb
manage.py convert_to_south myapp
manage.py migrate 0001 --fake


# Listing Current Migrations
manage.py migrate --list

# Discard migration
manage.py migrate name 0003 --fake

# Moving to 2 migration
manage.py migrate myapp 0002
manage.py migrate myapp						# moving to the next migration

# Creating own schema(e.g. datamigration)
manage.py datamigration myapp schema_name




I18n Translation(MultiLanguage)
##########################################################################################################
# In tempaltes:
{% load i18n %}

{% trans "Welcome to our page" %}
{% blocktrans %} {{ object }} details {% endblocktrans %}
# or
{{ form.instance.name|default:_('New Two for One promotion') }}

# In python code:
# Models - lazy
from django.utils.translation import ugettext_lazy as _
_('The file was successfully saved')

# Views
from django.utils.translation import ugettext as _
_('The file was successfully saved')


django-admin.py makemessages -l en           # Creating message files
django-admin.py makemessages -a              # Update/Reexamine all source code and templates

django-admin.py compilemessages              # Compiling message files
 ./manage.py compilemessages --locale=pl     # Compiling specify language

# For external applications add 'locale' folder to 'MANIFEST.in'




Templates
##########################################################################################################

# Blocks
{% extends "base.html" %}

{% include "messages.html" %}
# You can pass additional context to the template using keyword arguments:
{% include "name_snippet.html" with person="Jane" greeting="Hello" %}
# If you want to render the context only with the variables provided (or even no variables at all)
{% include "name_snippet.html" with greeting="Hi" only %}

{% load static %}
{% load staticfiles %}
{% static "css/base.css" %}

{% block content %} {% endblock %}

# block.super - get everything from original block
{% block title %}{{ block.super }} - {{ slug|capfirst }}{% endblock %}

# Url
{% url 'myapp:url-name' %}
# With additional parameters to url
<a href="{% url 'material' mat_cat_id=file.material_reference.get_category %}?mat_id={{ mat_id }}">
<form action="{% url 'url_name' %}?id={{ obj.pk }}" method="POST">

# Caches a complex variable under a simpler name(only between start and end tag)
{% with request.resolver.mach.url_name as urlname %}{% endwith %}

# Logic
{% for field in form %}
    {{ forloop.counter }}: {% field.label != 'user' and != 'material'}
{% empty %}
    <li>Sorry, no fields in this list.</li>
{% endfor %}

{% if article.count > 0 %}
{% else %}
{% endif %}

# Required field test
{% if form_experiment.name.field.required %}*{% endif %}

# Foreign Key
{% for a in article.comment_set.all %}
{% endfor %}

# Filters
{{ article.body|lower|truncatewords:"10"|truncatechars:120|timesince|urlize|linebreaks(białe znaki sa respektowane) }}

# Filters with function
{{ synth_obj.material.material_category.all|join:', ' }}

# Security
{% csrf_token %}

# Internet protocol
{% if request.is_secure %}https{% else %}http{% endif %}

# Form
<div class="fieldWrapper">
    {{ form.subject.errors }}
    {{ form.subject.label_tag }}
    {{ form.subject }}
</div>

# Form(with file upload)
<form action="/article/create/" method="POST/GET" enctype="multipart/form-data">
<input type="text" name="query" placeholder="Search posts" value="{{ request.GET.query }}" />

# Form errors
{{ form.non_field_errors }}

# Request/query
<a href="?{{ page }}={{ object.page_number }}{% if request.GET.query %}&query={{ request.GET.query }}{% endif %}">...</a>

# Verbatim
{% verbatim %} ... {% endverbatim %}



Views
##########################################################################################################
from django.contrib import messages
return render_to_response('experiments/management.html', ret, context_instance=RequestContext(request))
return HttpResponseRedirect(reverse('print_data') + '?' + urlencode(kwargs))
response = HttpResponse(mimetype='application/force-download')

return JsonResponse({'status': False, 'message': form.errors}, 'application/json', 200)


form = UserForm(data=request.GET/POST or None, files=request.FILES or None, instance=object_instance)
if form.is_valid(): 
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, 'Successfully created', extra_tags='class-name-tag')
    # we can put pure html in the message, then add extra_tags='html_safe', but in templates we need to use something like this:
    # {% if 'html_safe' in message.tags %} {{ message|safe }} {% else %} {{ message }} {% endif %}
    return HttpResponseRedirect(instance.get_absolute_url())
    return redirect('user_profile', id=instance.pk)

 



Forms
##########################################################################################################
from django.core.exceptions import ValidationError, ImproperlyConfigured

# Form class validation
def clean_user(self):
    user = self.cleaned_data['user']
    if self.instance:
        return user
    try:
        user = UserProfile.objects.get(pk=int(user))
    except UserProfile.DoesNotExists, TypeError:
        raise forms.ValidationError("Error")
    return user    								# or return self.cleaned_data if 'def clean(self):'

def clean(self):
    cleaned_data = super(CouponTemplateForm, self).clean()
    if not cleaned_data.get('value'):
        self._errors["value"] = self.error_class(
            [_('This field is required.')])
    return cleaned_data


# def __init__(self, *args, **kwargs):
# super(ClassName, self).__init__(*args, **kwargs)
self.fields['field_name'].label = commercial_label
self.fields['field_name'].initial = datetime.datetime.now()
self.fields['field_name'].disabled = True



# Widgets
publish = forms.DateField(widget=forms.SelectDateWidget)

# w = CalendarWidget()
# w.media
class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('pretty.css',)
        }
        js = ('animations.js', 'actions.js')



# django Pagedown widget
from pagedown.widgets import PagedownWidget
content = forms.CharField(widget=PagedownWidget)
# templates
{% block head_extra %}
    {{ form.media }}
{% endblock %}


Request
##########################################################################################################

request.META['HTTP_REFERER'].split('/')
request.FILES
request.method == "POST"
request.POST.get('username', '')
request.is_ajax()								# check HTTP_X_REQUESTED_WITH header for the string 'XMLHttpRequest'
#  e.g.
# form = UserForm(data=request.GET/POST or None, files=request.FILES or None, instance=object_instance)

request.user.is_staff
request.user.is_superuser
request.user.is_authenticated()

request.is_secure()
request.build_absolute_uri()                    # https://www.djangoproject.com/...
request.get_full_path()                         # /app_name/...

# Cookies
request.COOKIES['lang']
response.set_cookie('lang', language)

# Session
request.session['lang'] = language




Model objects (ORM object-relational mapper, mapowanie obiektowo-relacyjne)
##########################################################################################################

# Create
Article(title='Cheddar Talk', tagline='Thoughts on cheese.').save()			# Create new instance and save it into DB
Article.objects.create(title='Cheddar Talk', tagline='Thoughts on cheese.')
Object.save(update_fields=['title'])										# Update only 'title' column
# def save(commit=True, author=None, *args, **kwargs):                      # Remember about *args and **kwargs(especially with super)
#     art = super(Article, self).save(commit=False)
#     if author:
#         art.author = author
#     if commit:
#         art.save()
#         self.save_m2m()
#     return art

Article.objects.select_related().filter(blog=b).update(headline='Everything is the same')   # Updating multiple objects at once


# Filter
Article.objects.none()														# Empty queryset
Article.objects.filter(title__contains=search_text)
Article.objects.filter(headline__search="+Django -jazz Python")

Article.objects.filter(tagline__iregex=host_regex)
Article.objects.filter(author__book__title__icontains='element') - nierozroznialnosc wielkosci liter
Article.objects.filter(author__book__title__contains='element') - wazna wielkośc znaków

Entry.objects.filter(headline__iendswith='will')
Entry.objects.filter(headline__endswith='cats')
Entry.objects.filter(headline__istartswith='will')
Entry.objects.filter(headline__startswith='will')

Entry.objects.filter(pub_date__range=(start_date, end_date))



# Select related (ForeignKey or OneToOneField)
# Returns a QuerySet that will “follow” foreign-key relationships,
# selecting additional related-object data when it executes its query.
# This is a performance booster which results in a single more complex query
# but means later use of foreign-key relationships won’t require database queries.
Entry.objects.select_related('blog').get(id=5)
Entry.objects.filter(pub_date__gt=timezone.now()).select_related('blog')
Book.objects.select_related('author__hometown').get(id=4)



# Prefetch related (ManyToMany and ManyToOne)
# Returns a QuerySet that will automatically retrieve, in a single batch,
# related objects for each of the specified lookups
Pizza.objects.all().prefetch_related('toppings')
Restaurant.objects.prefetch_related('best_pizza__toppings')
Restaurant.objects.select_related('best_pizza').prefetch_related('best_pizza__toppings')



# Annotates each object in the QuerySet with the provided list of query expressions. Eexpression may be a simple value,
# a reference to a field on the model (or any related models), or an aggregate expression (averages, sums, etc.)
queryset.annotate(num_photos=models.Count('moviephoto')).filter(num_photos__gte=2)

Entry.objects.get(title__regex=r'^(An?|The) +')                             # Case-sensitive regular expression match
Entry.objects.get(title__iregex=r'^(an?|the) +')                            # Case-insensitive regular expression match



Entry.objects.values('name', 'entry__headline')                             # values => list of dictionaries
# [{'name': 'My blog', 'entry__headline': 'An entry'}, {'name': 'My blog', 'entry__headline': 'Another entry'}, ...]

Entry.objects.values_list('id').order_by('id')                              # values_list => list of tuples
# [(1,), (2,), (3,), ...]
Entry.objects.values_list('id', flat=True).order_by('id')
# [1, 2, 3, ...]

# Flat - if you only pass in a single field, you can also pass in the flat parameter.
# If True, this will mean the returned results are single values, rather than one-tuples

# Queryset difference – a difference (mathematically written as qs1\qs2) is all the items in qs1 that do not exist in qs2.
qs1.exclude(pk__in=qs2)



# Q object (OR)
from django.db.models import Q
queryset.filter(
    Q(question__startswith='What') |
    Q(title__icontains=query) |
    Q(user__first_name__icontains=query)
    ).distinct()

biq_Q = Q()
for exp_type in data.get('experiment_type'):
    big_Q |= Q(inny_arg="cos")
ctx['files'] = ctx['files'].filter(big_Q)



# Extra queryset
Entry.objects.extra(select={'is_recent': "pub_date > '2006-01-01'"})
Blog.objects.extra(
    select={
        'entry_count': 'SELECT COUNT(*) FROM blog_entry WHERE blog_entry.blog_id = blog_blog.id'
    },
)
Entry.objects.extra(where=["foo='a' OR bar = 'a'", "baz = 'a'"])	# SELECT * FROM blog_entry WHERE (foo= 'a' OR bar='a') AND (baz='a')



# Model fields
title = models.CharField(
    max_length=25,
    db_index=True,
    unique=True,
    null=True,
    blank=True,
    default=None,
    editable=False)

update = models.DateTimeField(
    default=datetime.now().strftime("%Y-%m-%d,%H:%M:%S.%f")[:-3],
    auto_now=True,                  # when updated
    auto_now_add=False)             # when created

create_time = models.DateTimeField(
	default=datetime.now().strftime("%Y-%m-%d,%H:%M:%S.%f")[:-3],
    auto_now=False,
    auto_now_add=True)

# from django.contrib.auth import get_user_model
# User = get_user_model()
user = models.ForeignKey(User, on_delete=models.PROTECT, default=1) # CASCADE(default), SET_NULL
parent = models.ForeignKey('self', null=True, blank=True)

sections = models.ManyToManyField(Section,
    limit_choices_to=Q(name__iendswith='_banner') | Q(name__iendswith='_box') | Q(element_parent__isnull=False))

info_file = models.FileField(max_length=250, upload_to=get_upload_path, validators=[])
# def get_upload_path(instance, filename):
#     """
#     This function return path for filename
#     :param instance: instance of model
#     :param filename: name of new file
#     :return: path where file can be saved
#     """
#     return os.path.join(str(instance.experiment.id),
#                         str(instance.material.id),
#                         filename)

image = models.ImageField(
    upload_to=upload_location,                  # relative to media uploads
    null=True,
    blank=True,
    width_field='width_field',
    height_field='height_field')
width_field = models.IntegerField(default=0)
height_field = models.IntegerField(default=0)



# Meta
class Meta:
    ordering = ['id']  # postgres => query_set => models => ordering
    verbose_name = _('content type')
    verbose_name_plural = _('content types')
    db_table = 'django_content_type'
    unique_together = (('app_label', 'model'),)



# Model manager (working with querysets)
class PostManager(models.Manager):
    def all(self, *args, **kwargs):
        # Post.post_objects.all() == super(PostManager, self).all()
        ...

    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timzone.now())


class Post(models.Model):
    ...
    post_objects = PostManager()               # objects is default manager, e.g: Post.objects.all()
                                               # we can overwrite default behavior of the manager


Post.post_objects.all()




Django Generic Foreign Key (Django Content Type)
##########################################################################################################
# content_type_field => manager with qs => model property => instance.property in templates
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Comment
class CommentManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs


class Comment(models.Model):
    ...
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = CommentManager()


# Post
class Post(models.Model):
    ...

    @property
    def comments(self):
        qs = Comment.objects.filter_by_instance(self)
        return qs




Pre and Post save
##########################################################################################################
from django.db.models.signals import pre_save

def pre_save_receiver(sender, instance, *args, **kwargs):
    ...


pre_save.connect(pre_save_receiver, sender=model_name)




Django Utilities
##########################################################################################################

# Time
from django.utils import timezone
date_time = models.DateTimeField(default=timezone.now)		# Without parenthesis, create function and 
#															  then in the view call it

# Slugify
from django.utils.text import slugify
slug = models.SlugField(unique=True)

slugify('Tesla motor 1')                                    # 'tesla-motor-1'




Django Statics
##########################################################################################################
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')                                    # Django server
]                                                                       # From django server => manage.py collectstatic => static server
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn')     # Static server

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




Authentication and User
##########################################################################################################
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
user = auth.authenticate(username=username, password=password)
auth.login(request, user)
auth.logout(request)




Admin
#####################################################f#####################################################
from django.contrib import admin
from .models import Post
 
class PostModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['updated']
    list_editable = ['title']

    list_filter = ['update', 'timestamp']

    search_fields = ['title', 'content']

    form = CustomiseFormClass

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)




Urls
##########################################################################################################
from django.core.urlresolvers import reverse, resolve
reverse('admin:app_list', kwargs={'app_label': 'auth'})

func, args, kwargs = resolve('/some/path/')

url(r'^image/', include('image.urls', namespace='image'))
url(r'^(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder')

# url with class method
def get_absolute_url(self):
    return reverse('image:placeholder', kwargs={'width': self.width, 'height': self.height})

# templates
{% url 'image:placeholder' width=obj.width height=obj.height %}
or
{{ obj.get_absolute_url }}

# view errors
handler400 = 'mysite.views.my_custom_bad_request_view'                  # bad_request()
handler403 = 'mysite.views.my_custom_permission_denied_view'            # permission_denied()
handler404 = 'mysite.views.my_custom_page_not_found_view'               # page_not_found()
handler500 = 'mysite.views.my_custom_error_view'                        # server_error()






File 'import' structure
##########################################################################################################
# -*- coding: UTF-8 -*-
# biblioteki systemowe
import os
# biblioteki zewnętrzne
from PIL import Image
# moduły Django
from django.conf import settings
# aplikacje Django
from cms.models import Page
# moduły bieżącej aplikacji
import app_settings




Django settings
##########################################################################################################
/django/conf/global_settings.py
/django/conf/project_template/project_name/settings.py-tpl

LOGIN_REDIRECT_URL = '/'
ADMINS = (('name', 'email'),)           # if errors e.g. 400, 403, 404, 500, those admins get emails




# To Do
from django.contrib.auth.models import Group
from django.db.models.query import CollectedObjects
from django.db.models.fields.related import ForeignKey
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_str, force_unicode
from django.utils.html import strip_tags

django_markdown
django_markdown_deux

<a href="{% url 'admin:index' %}">{% trans 'Home' %}</a>
<a href="{% url 'admin:app_list' app_label=opts.app_label %}">{{ opts.app_config.verbose_name }}</a>
{% if has_change_permission %}<a href="{% url opts|admin_urlname:'changelist' %}">{{ opts.verbose_name_plural|capfirst }}</a>{% else %}{{ opts.verbose_name_plural|capfirst }}{% endif %}

&rsaquo; {% if add %}{% trans 'Add' %} {{ opts.verbose_name }}{% else %}{{ original|truncatewords:"18" }}{% endif %}

# Production/Beta
raise Warning, jakaś_zmienna

mysqldump -u USERNAME -pPASSWORD DATABASE_NAME > DATABASE_FILE.sql
python manage.py dbshell < ~/db_backups/db.sql


# Cache template fragment
{% load cache %}
    {% cache 500 sidebar request.user.username %}
        .. sidebar for logged in user ..
{% endcache %}




# TO DO
{% include "delete_modal.html" with obj_name=_("discount") %}

{% if forloop.last %} class='last'{% endif %}>{{ item }}

LicenseKey.objects.values('value').annotate(total=Count('value')).filter(total=2)
