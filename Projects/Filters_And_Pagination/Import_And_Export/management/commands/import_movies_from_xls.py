# -*- coding: UTF-8 -*-
# pip install xlrd
import xlrd

from django.core.management.base import BaseCommand, CommandError
from django.utils.encoding import smart_str
from movies.models import Movie

SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3


class Command(BaseCommand):
	args = "<file_path>"
	help = "Importuje informacje o filmach z lokalnego pliku XLS. Wymaga podania tytułu, adresu URL i daty premiery."

	def handle(self, *args, **options):
		verbosity = int(options.get("verbosity", NORMAL))
		if args:
			file_path = args[0]
		else:
			raise CommandError("Podaj ścieżkę do pliku XLS.")

		wb = xlrd.open_workbook(file_path)
		sh = wb.sheet_by_index(0)

		if verbosity >= NORMAL:
			print("=== Filmy zaimportowane ===")
		for rownum in range(sh.nrows):
			if rownum > 0:
				(title, url, release_year) = sh.row_values(rownum)
				movie, created = Movie.objects.get_or_create(
					title=title,
					url=url,
					release_year=release_year,
				)
				if verbosity >= NORMAL:
					print(" - " + smart_str(movie.title))

# python manage.py import_movies_from_xls data/movies.xls
