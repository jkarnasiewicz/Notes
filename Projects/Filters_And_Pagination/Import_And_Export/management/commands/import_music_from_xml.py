# -*- coding: UTF-8 -*-
import os
import requests
from xml.etree import ElementTree
from StringIO import StringIO

from django.core.management.base import BaseCommand, CommandError
from django.utils.encoding import smart_str, force_unicode
from django.conf import settings
from django.core.files import File

from music.models import Track

SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3

class Command(BaseCommand):
	args = "<file_path>"
	help = "Importuje utwory z portalu Last.fm w formacie XML."

	def handle(self, *args, **options):
		self.verbosity = int(options.get("verbosity", NORMAL))

		r = requests.get("http://ws.audioscrobbler.com/2.0/", params={
			"method": "tag.gettoptracks",
			"tag": "disco",
			"api_key": settings.LAST_FM_API_KEY,
		})

		root = ElementTree.fromstring(r.content)
		total_pages = int(root.find("toptracks").attrib["totalPages"])

		if self.verbosity >= NORMAL:
			print("=== Ścieżki zaimportowane ===")

		self.save_page(root)

		for page_number in range(2, total_pages + 1):
			r = requests.get("http://ws.audioscrobbler.com/2.0/", params={
				"method": "tag.gettoptracks",
				"tag": "disco",
				"api_key": settings.LAST_FM_API_KEY,
				"page": page_number,
			})
			root = ElementTree.fromstring(r.content)
			self.save_page(root)

	def save_page(self, root):
		for track_node in root.findall("toptracks/track"):
			track = Track()
			track.name = force_unicode(track_node.find("name").text)
			track.artist = force_unicode(track_node.find("artist/name").text)
			track.url = force_unicode(track_node.find("url").text)
			track.save()
			image_node = track_node.find("image[@size='medium']")
			if image_node is not None:
				image_response = requests.get(image_node.text)
				track.image.save(
					os.path.basename(image_node.text),
					File(StringIO(image_response.content))
				)

			if self.verbosity >= NORMAL:
				print(smart_str(" - %s - %s" % (track.artist, track.name)))

# python manage.py import_music_from_xml
