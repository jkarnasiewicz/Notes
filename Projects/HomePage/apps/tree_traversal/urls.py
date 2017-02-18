from django.conf.urls import url
from .views import tree_traversal

urlpatterns = [
	url(r'^$', tree_traversal, name='tree_traversal'),
	# url(r'^add_catalog/$', add_catalog, name='add_catalog'),
	# url(r'^add_file/$', add_file, name='add_file'),
]