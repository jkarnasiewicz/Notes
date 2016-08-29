# -*- coding: UTF-8 -*-
# pip install requests
import os
import requests

from StringIO import StringIO
from django.core.management.base import BaseCommand, CommandError
from django.utils.encoding import smart_str, force_unicode
from django.conf import settings
from django.core.files import File
from music.models import Track

SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3

class Command(BaseCommand):
	args = "<file_path>"
	help = "Importuje 10 najpopularniejszych ścieżek z portalu last.fm w formacie XML."

	def handle(self, *args, **options):
		self.verbosity = int(options.get("verbosity", NORMAL))

		r = requests.get("http://ws.audioscrobbler.com/2.0/", params={
			"method": "tag.gettoptracks",
			"tag": "disco",
			"api_key": settings.LAST_FM_API_KEY,
			"format": "json",
		})

		response_dict = r.json()
		total_pages = int(response_dict["toptracks"]["@attr"]["totalPages"])

		if self.verbosity >= NORMAL:
			print("=== Ścieżki zaimportowane ===")

		self.save_page(response_dict)

		for page_number in range(2, total_pages + 1):
			r = requests.get("http://ws.audioscrobbler.com/2.0/", params={
				"method": "tag.gettoptracks",
				"tag": "disco",
				"api_key": settings.LAST_FM_API_KEY,
				"page": page_number,
			})
			response_dict = r.json()
			self.save_page(response_dict)

	def save_page(self, d):
		for track_dict in d["toptracks"]["track"]:
			track = Track()
			track.name = force_unicode(track_dict["name"])
			track.artist = force_unicode(track_dict["artist"]["name"])
			track.url = force_unicode(track_dict["url"])
			track.save()
			image_dict = track_dict.get("image", None)
			if image_dict:
				image_url = image_dict[1]["#text"]
				image_response = requests.get(image_url)
				track.image.save(
					os.path.basename(image_url),
					File(StringIO(image_response.content))
				)
			if self.verbosity >= NORMAL:
				print(smart_str(" - %s - %s" % (track.artist, track.name)))

# python manage.py import_music_from_json
