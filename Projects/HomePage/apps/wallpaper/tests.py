from django.test import TestCase
from django.core.urlresolvers import reverse

from .forms import WallpaperForm
from .views import wallpaper


class ViewTest(TestCase):

	def test_wallpaper_page_usess_correct_view(self):
		response = self.client.get(reverse('wallpaper:wallpaper'))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.resolver_match.func, wallpaper)

	def test_wallpaper_page_render_correct_tamplates(self):
		response = self.client.get(reverse('wallpaper:wallpaper'))

		self.assertTemplateUsed(response, 'wallpaper/home.html')

	def test_wallpaper_page_uses_correct_form(self):
		response = self.client.get(reverse('wallpaper:wallpaper'))

		self.assertIsInstance(response.context['form'], WallpaperForm)
