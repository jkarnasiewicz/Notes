# -*- coding: UTF-8 -*-
import csv

from django.core.management.base import BaseCommand, CommandError
from django.utils.encoding import smart_str

from Import_And_Export.models import Movie

SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3


class Command(BaseCommand):
	args = "<file_path>"
	help = "Importuje informacje o filmach z lokalnego pliku csv. Wymaga podania tytułu, adresu URL i daty premiery."

	def handle(self, *args, **options):
		verbosity = int(options.get("verbosity", NORMAL))
		if args:
			file_path = args[0]
		else:
			raise CommandError("Podaj ścieżkę do pliku CSV.")

		if verbosity >= NORMAL:
			print("=== Filmy zaimportowane ===")

		with open(file_path) as f:
			reader = csv.reader(f)
			for title, url, release_year in reader:
				movie, created = Movie.objects.get_or_create(
					title=title,
					url=url,
					release_year=release_year)
				if verbosity >= NORMAL:
					print(" - " + smart_str(movie.title))

# python manage.py import_movies_from_csv data/movies.csv
