from django.conf.urls import patterns, url
from .views import movie_category_list

urlpatterns = [
	url(r'^$', movie_category_list, name='movie_category_list'),
]