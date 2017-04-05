from django.conf.urls import url

from .views import scikit_chart


urlpatterns = [
	url(r'^$', scikit_chart, name='scikit_chart'),
]
