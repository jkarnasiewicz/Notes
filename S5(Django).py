# General information

# creating project "mysite"
django-admin.py startproject mysite
# creating new app named myapp
./manage.py startapp myapp



# run development server / python manage.py runserver 8080
./manage.py runserver
# run with specify settings file
./manage.py runserver --settings=settings.production
# run in insecure mode and serve static locally (e.g. for testing without debug)
./manage.py runserver --insecure



# shell, pip install ipython (improve shell), help('django.forms'), help(ModelForm)
./manage.py shell

# run the command-line client for the database engine specified in your ENGINE setting
./manage.py dbshell < ~/db_backups/db.sql


# sql for model_name class
./manage.py sql model_name
# reset all the data and update model schema
./manage.py reset model_name



# export all data to file db_backup.json
./manage.py dumpdata --indent=2 > db_backup.json
./manage.py dumpdata offers.District --exclude=auth --exclude=contenttypes > db_test.json
# import data from db_backup.json
./manage.py loaddata db_backup.json



# show django models.py for specify databse
./manage.py inspectdb --database=external_db
# copy to models.py file
./manage.py inspectdb > models.py



# Test whole project with verbosity level(0-3)
./manage.py test -v3
# Test only myapp
./manage.py test myapp
# Preserving test database
./manage.py test -v3 --keepdb
# Specify custom filename pattern
./manage.py test --pattern="tests_*.py"
# Runs tests in separate parallel processes(--parallel=4, or by setting the DJANGO_TEST_PROCESSES)
./manage.py test --parallel
# The -Wall flag tells Python to display deprecation warnings
python -Wall manage.py test



# Collect all the static files
./manage.py collectstatic --noinput
# Creating new permissions define in xml file
./manage.py createpermissions
./manage.py createsuperuser



# Help for additional management command(update)
./manage.py update --help



# Migrations (tables with migrated schemas: django_migrations)
./manage.py makemigrations
./manage.py migrate
./manage.py showmigrations

./manage.py migrate --fake
./manage.py migrate --fake-initial



# Custom function in migration files
./manage.py makemigrations app_name --empty     # Create empty migration file
operation = [
    migrations.RunPython(find_duplicates),
]










# Models (ORM object-relational mapper, mapowanie obiektowo-relacyjne)

# W systemie Django wyróżnia się trzy typy dziedziczenia modeli:
# abstrakcyjne klasy bazowe (Abstract base classes),
# dziedziczenie wielotabelowe (Multi-table inheritance or concrete) oraz modele proxy (Proxy models)

# Domieszki(Mixins) modeli są abstrakcyjnymi klasami modeli z określonymi polami, własnościami i metodami
# Mixins encourage code reuse. A mixin can also be viewed as an interface with implemented methods

# Concrete - each model corresponds to its own database table and can be queried and created individually
# The inheritance relationship introduces links between the child model and each of its parents
# (via an automatically-created OneToOneField)

# Creating a proxy for the original model. You can create, delete and update instances of the proxy model
# and all the data will be saved as if you were using the original (non-proxied) model

class Meta:
    verbose_name = _(u"Pomysł")
    verbose_name_plural = _(u"Pomysły")
    abstract = True
    proxy = True

    # ordering options: field_name(ascending), -field_name(descending) or ?(random)
    ordering = ('id',)                                  # database(postgres) => query_set => models => ordering
    unique_together = (('app_label', 'model'),)         # unique_together also influence qs ordering
    db_table = 'django_content_type'



# Create

# create new instance and save it into DB
# !!! note that full_clean() will not be called automatically when you call model’s save()
# or create method. You’ll need to call it manually
# full_clean() calls: Model.clean_fields(), Model.clean(), Model.validate_unique()
Article(title='Cheddar Talk', tagline='Thoughts on cheese.').save()
Article.objects.create(title='Cheddar Talk', tagline='Thoughts on cheese.')

# get or create object
obj, created = Article.objects.get_or_create(**kwargs, default_dict)

# update only 'title' column
object.save(update_fields=['title'])

# updating multiple objects at once
Article.objects.select_related().filter(blog=b).update(headline='Everything is the same')



# remember about *args and **kwargs(especially with super)
def save(commit=True, author=None, *args, **kwargs):
    art = super(Article, self).save(commit=False)
    if author:
        art.author = author
    if commit:
        art.save()
        self.save_m2m()
    return art



# bulk_create inserts the provided list of objects into the database in an efficient manner(generally only 1 query)
# the model’s save() method will not be called, and the pre_save and post_save signals will not be sent
bulk_create(objs, batch_size=None)

Item.objects.bulk_create([
    Item(headline='This is a test'),
    Item(headline='This is only a test')])



# This will run on the 'default' database
Author.objects.all()

# So will this
Author.objects.using('default').all()

# This will run on the 'other' database.
Author.objects.using('other').all()

# To save an object to the legacy_users database
object.save(using='legacy_users')



# Filter
# queryset(lazy objects) - keep QuerySets unevaluated as long as possible

# empty queryset
Article.objects.none()
Article.objects.filter(title__contains=search_text)
Article.objects.filter(headline__search="+Django -jazz Python")

Article.objects.get(title__iregex=r'^(an?|the) +')                          # Case-insensitive regular expression match (nieistotna wielkosci liter)
Article.objects.get(title__regex=r'^(An?|The) +')                           # Case-sensitive regular expression match (istotna wielkośc znaków)

Article.objects.filter(author__book__title__icontains='element') 
Article.objects.filter(author__book__title__contains='element')

Entry.objects.filter(headline__iendswith='will')
Entry.objects.filter(headline__endswith='cats')

Entry.objects.filter(headline__istartswith='will')
Entry.objects.filter(headline__startswith='will')

Entry.objects.filter(pub_date__range=(start_date, end_date))

# queryset difference – a difference (mathematically written as qs1\qs2) is all the items in qs1 that do not exist in qs2
qs1.exclude(pk__in=qs2)



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
Entry.objects.values('value').annotate(total=Count('value')).filter(total=2)
Entry.objects.values('slug').annotate(Count('id')).order_by().filter(id__count__gt=1)



# values => list of dictionaries
Entry.objects.values('name', 'entry__headline')
# [{'name': 'My blog', 'entry__headline': 'An entry'}, {'name': 'My blog', 'entry__headline': 'Another entry'}, ...]


# values_list => list of tuples
Entry.objects.values_list('id').order_by('id')
# [(1,), (2,), (3,), ...]
Entry.objects.values_list('id', flat=True).order_by('id')
# [1, 2, 3, ...]

# Flat - if you only pass in a single field, you can also pass in the flat parameter.
# If True, this will mean the returned results are single values, rather than one-tuples



# Chaining multiple QuerySets(from different models)
from itertools import chain
recent = chain(qs1, qs2)
sorted(recent, key=lambda e: e.modified, reverse=True)[:3]



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
Entry.objects.extra(where=["foo='a' OR bar = 'a'", "baz = 'a'"])    # SELECT * FROM blog_entry WHERE (foo= 'a' OR bar='a') AND (baz='a')



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

# remove auto id field with primary_key
email = models.EmailField(primary_key=True)

user = models.ForeignKey(User, on_delete=models.PROTECT, default=1)                 # CASCADE(default), SET_NULL
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





# Pre and Post save
from django.db.models.signals import pre_save

def pre_save_receiver(sender, instance, *args, **kwargs):
    ...

pre_save.connect(pre_save_receiver, sender=model_name)





# Model manager (working with querysets)
class PostManager(models.Manager):
    def all(self, *args, **kwargs):
        # Post.post_objects.all() == super(PostManager, self).all()
        ...

    def active(self, *args, **kwargs):
        # return super(PostManager, self).filter(draft=False).filter(publish__lte=timzone.now())
        return self.filter(draft=False).filter(publish__lte=timzone.now())


class Post(models.Model):
    # objects is default manager, e.g: Post.objects.all()
    # we can overwrite default behavior of the manager
    post_objects = PostManager()

Post.post_objects.all()










# Views

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse, JsonResponse
from django.shortcuts import render_to_response, render, redirect

from django.template import RequestContext
from django.template.loader import render_to_string

# an HTTP response class with a string as content
HttpResponse(mimetype='application/force-download')
HttpResponseRedirect(reverse('print_data') + '?' + urlencode(kwargs))

# streaming data
StreamingHttpResponse(stream_response_generator())

# json
JsonResponse({'status': False, 'message': form.errors}, 'application/json', 200)
# HttpResponse(' ', content_type="application/json")



# shortcuts
render_to_response('template_name.html', ctx, context_instance=RequestContext(request))
render(request, 'template_name.html', ctx)

redirect('user_profile', id=instance.pk)
redirect(instance)                              # this calls instance.get_absolute_url()



# loads a template and renders it with a context, returns a string
render_to_string(template_name, context=None, request=None, using=None)



form = UserForm(data=request.GET/POST or None, files=request.FILES or None, instance=object_instance)
if form.is_valid(): 
    instance = form.save(commit=False)
    ...
    instance.save()
    messages.success(request, 'Successfully created', extra_tags='class-name-tag')
    # we can put pure html in the message, then add extra_tags='html_safe', but in templates we need to use something like this:
    # {% if 'html_safe' in message.tags %} {{ message|safe }} {% else %} {{ message }} {% endif %}
    return HttpResponseRedirect(instance.get_absolute_url())










# Forms

from django import forms
from django.core.exceptions import ValidationError, ImproperlyConfigured

def __init__(self, owner, *args, **kwargs):
    # super(ClassName, self).__init__(*args, **kwargs)      # python 2
    super().__init__(*args, **kwargs)                       # python 3
    self.instance.owner = owner
    self.fields['field_name'].label = 'label_name'
    self.fields['field_name'].initial = datetime.datetime.now()
    self.fields['field_name'].disabled = True

def clean_user(self):
    user = self.cleaned_data['user']
    if self.instance:
        return user
    try:
        user = UserProfile.objects.get(pk=int(user))
    except UserProfile.DoesNotExists, TypeError:
        raise forms.ValidationError("Error")
    return user

def clean(self):
    cleaned_data = super(ClassName, self).clean()
    if not cleaned_data.get('value'):
        self._errors["value"] = self.error_class(
            [_('This field is required.')])
    return cleaned_data



# Przekazywanie całego reqesta do formularza
# forms.py
class MessageForm(forms.Form):
    # ...
    def __init__(self, request, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.request = request
        self.fields['recipient'].queryset = self.fields['recipient'].queryset.exclude(pk=request.user.pk)

# views.py
def message_to_user(request):
    if request.method == "POST":
        form = MessageForm(request, data=request.POST)
        if form.is_valid():                                 # == calling form.full_clean() directly trigger cleaning and validation
            # ...
            return redirect("message_to_user_done")
    else:
        form = MessageForm(request)
    return render(request, "email_messages/message_to_user.html", { 'form': form })



# Widgets
publish = forms.DateField(widget=forms.SelectDateWidget)

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        exclude = ('material_instance',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'To Do list',
                'class': 'form-control input-lg'
                })
        }

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










# Templates
# keep business logic out of your templates

from django.template import Template, Context
Template("<h1>{{ title }}</h1>").render(Context({"title": "SuperBook"}))                    # => '<h1>SuperBook</h1>'

{% extends "base.html" %}

{% include "messages.html" %}
# You can pass additional context to the template using keyword arguments:
{% include "name_snippet.html" with person="Jane" greeting=_("Hello") %}
# If you want to render the context only with the variables provided (or even no variables at all)
{% include "name_snippet.html" with greeting="Hi" only %}



# static
{% load static %}
# {% load staticfiles %}
<link href="{% static 'css/base.min.css' %}" rel="stylesheet">



# blocks
{% block content %} {% endblock %}

# block.super - get everything from original block
{% block title %}{{ block.super }} - {{ slug|capfirst }}{% endblock %}



# url
{% url 'myapp:url-name' %}

# with additional parameters to url
<a href="{% url 'material' mat_cat_id=file.material_reference.get_category %}?mat_id={{ mat_id }}">
<form action="{% url 'url_name' %}?id={{ obj.pk }}" method="POST">



# caches a complex variable under a simpler name(only between start and end tag)
{% with request.resolver.mach.url_name as urlname %}{% endwith %}

# cache template fragment
{% load cache %}
    {% cache 500 sidebar request.user.username %}
        .. sidebar for logged in user ..
{% endcache %}



# for
{% for field in form %}
    {{ forloop.counter }}: {% field.label != 'user' and != 'material'}
    {% if forloop.last %} class='last'{% endif %}
{% empty %}
    <li>Sorry, no fields in this list.</li>
{% endfor %}



# if-else
{% if article.count > 0 %}
{% else %}
{% endif %}



# filters
{{ article.body|lower|truncatewords:"10"|truncatechars:120|timesince|urlize|linebreaks(białe znaki sa respektowane) }}

# filters with function
{{ synth_obj.material.material_category.all|join:', ' }}



# form
<div class="fieldWrapper">
    {{ form.subject.errors }}
    {{ form.subject.label_tag }}
    {{ form.subject }}
</div>

# form(with file upload)
<form action="/article/create/" method="POST/GET" enctype="multipart/form-data">
<input type="text" name="query" placeholder="Search posts" value="{{ request.GET.query }}" />

# form errors
{{ form.non_field_errors }}

{% if form.errors %}                                                # all errors for this form
    <div class='form-group has-error'>
        <div class='help-block'>{{ form.text.errors }}</div>        # only text field errors
    </div>
{% endif %}

# required field test
{% if form_experiment.name.field.required %}*{% endif %}



# security(Cross-Site Request Forgery)
{% csrf_token %}                                        # full html tag
{{ csrf_token }}                                        # unmodified token string



# internet protocol
{% if request.is_secure %}https{% else %}http{% endif %}

# date tag
Date is {% now 'd-m-Y' %}

# foreign key
{% for a in article.comment_set.all %}
{% endfor %}

# request/query
<a href="?{{ page }}={{ object.page_number }}{% if request.GET.query %}&query={{ request.GET.query }}{% endif %}">...</a>

# verbatim, stops the template engine from rendering the content of this block tag
{% verbatim %} ... {% endverbatim %}










# I18n Translation(MultiLanguage)

# In tempaltes:
{% load i18n %}

{% trans "Welcome to our page" %}
{% blocktrans %} {{ object }} details {% endblocktrans %}
# or
{{ form.instance.name|default:_('New item') }}



# In python code:
# Models - lazy
from django.utils.translation import ugettext_lazy as _
_('The file was successfully saved')

# Views
from django.utils.translation import ugettext as _
_('The file was successfully saved')



# Creating message files
django-admin.py makemessages -l en

# Update/Reexamine all source code and templates
django-admin.py makemessages -a



# Compiling message files
django-admin.py compilemessages

# Compiling specify language
./manage.py compilemessages --locale=pl

# For external applications add 'locale' folder to 'MANIFEST.in'










# Urls

from django.conf.urls import url
from django.core.urlresolvers import reverse, resolve

# reverse - first argument can be a URL pattern name or the callable view object
reverse('admin:app_list', kwargs={'app_label': 'auth'})
reverse(view.app_list, kwargs={'app_label': 'auth'})

# resolve - first argument is the URL path you want to resolve
func, args, kwargs = resolve('/some/path/')



# url conf
urlpatterns  = [
    url(r'^image/', include('image.urls', namespace='image')),
    url(r'^(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
]

# url with class method
def get_absolute_url(self):
    return reverse('image:placeholder', kwargs={'width': self.width, 'height': self.height})    # args=[self.id]

# templates
{% url 'image:placeholder' width=obj.width height=obj.height %}
or
{{ obj.get_absolute_url }}



# view errors
handler400 = 'mysite.views.my_custom_bad_request_view'                  # bad_request()
handler403 = 'mysite.views.my_custom_permission_denied_view'            # permission_denied()
handler404 = 'mysite.views.my_custom_page_not_found_view'               # page_not_found()
handler500 = 'mysite.views.my_custom_error_view'                        # server_error()










# Request

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
# if not request.user.is_authenticated():
#     raise PermissionDenied



request.is_secure()                             # https or http
request.build_absolute_uri()                    # https://www.djangoproject.com/...
request.get_full_path()                         # /app_name/...



# Cookies
request.COOKIES.get('lang', '')
request.get_signed_cookie('lang', '', salt=settings.COOKIES_KEY)

response.set_cookie('lang', language)
response.set_signed_cookie('lang', language, salt=settings.COOKIES_KEY, max_age=None, expires=None, path='/', domain=None, secure=None, httponly=True)



# Session
request.session['lang'] = language










# Authentication and User

from django.contrib import auth
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group                          # fields: name, permissions
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
User = get_user_model()

# custom user model
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = (
    'accounts.authentication.CustomAuthenticationBackend',
)



# authenticate
user = auth.authenticate(username=username, password=password)
auth.login(request, user)
auth.logout(request)










# Django Generic Foreign Key (Django Content Type)

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










# Django Utilities

# Time
from django.utils import timezone
# Without parenthesis, create function and then in the view call it
date_time = models.DateTimeField(default=timezone.now)



# Slugify
from django.utils.text import slugify
slug = models.SlugField(unique=True)

slugify('Tesla motor 1')                                    # => 'tesla-motor-1'



# Escape characters - returns the given text with ampersands, quotes and angle brackets encoded for use in HTML
from django.utils.html import escape
escape("q'<>&s")



# Tries to remove anything that looks like an HTML tag from the string, that is anything contained within <>
from django.utils.html import strip_tags
strip_tags('string')


# Explicitly mark a string as safe for (HTML) output purposes
from django.utils.safestring import mark_safe
mark_safe('string')










# Admin

from django.contrib import admin
from .models import Post
# default admin.site.register(Post)
 
class PostModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['updated']
    list_editable = ['title']

    ordering = ['updated']
    list_filter = ['update', 'timestamp']

    search_fields = ['title', 'content']

    form = CustomiseFormClass

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)


# in model class add:
# better presentation
def __str__()

# This attribute is handy if you like to switch between
# the admin view and the object's detail view on your website. If this method
# is defined, then a button labelled "View on site" will appear in the top
# right-hand side of the object's edit page in its admin page.
def get_absolute_url()

# Without this meta option, your entries can appear in any order as
# returned from the database
ordering

# If you omit this attribute, your model's name would be
# converted from CamelCase into camel case
verbose_name and verbose_name_plural

# in main urls add:
admin.site.site_header = "Secret Area"

# admin templates
django/contrib/admin/templates/admin










# Django settings

# /django/conf/global_settings.py
# /django/conf/project_template/project_name/settings.py-tpl

LOGIN_REDIRECT_URL = '/'

ADMINS = (('name', 'email'),)           # if errors e.g. 400, 403, 404, 500, those admins get emails



# Static

STATIC_URL = '/static/'                                                 # Urls for static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')                                    # Django server
]                                                                       # From django server => manage.py collectstatic => static server
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn')     # Static server

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










# Django DB

# Working with MySQL DB
apt-get install python-mysqldb
apt-get install build-essential python-dev libmysqlclient-dev
pip install MySQL-python

mysqldump -u USERNAME -p PASSWORD DATABASE_NAME > DATABASE_FILE.sql



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










# South

# Creating necessary db for settings.py
python manage.py syncdb
python manage.py syncdb --database=external_db

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
manage.py migrate myapp                     # moving to the next migration

# Creating own schema(e.g. datamigration)
manage.py datamigration myapp schema_name










# File 'import' structure

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










# apps.py

This file is created to help the user include any application configuration for the app.
Using this, you can configure some of the attributes of the application.
Application configuration objects store metadata for an application.
Some attributes can be configured in AppConfig subclasses. Others are set by Django and read-only.

Previously, there was no specific place for initializing the signal code. Typically, they
were imported or implemented in models.py (which was unreliable)










# Additional informations
# Tworzenie domieszek do modeli do obsługi relacji generycznych (Django - Najlepsze receptury 46)
# Wysyłanie obrazów na serwer i tworzenie miniatur obrazow (Django - Najlepsze receptury 66)
