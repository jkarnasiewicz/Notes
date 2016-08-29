from django.conf.urls import patterns, url
from .views import home, movie_detail_modal, json_set_like

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r"^movie_detail_modal/(?P<pk>\d+)/$", movie_detail_modal, name="movie_detail_modal"),
	url(r"^(?P<content_type_id>[^/]+)/(?P<object_id>[^/]+)/$", json_set_like, name="json_set_like"),
]