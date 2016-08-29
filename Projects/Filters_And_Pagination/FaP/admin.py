import xlwt

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin, User, Group
from django.http import HttpResponse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .models import Genre, Director, Actor, Movie, MoviePhoto


class GenreAdmin(admin.ModelAdmin):
	# fields = ['title']				# form fields for creating new entries
	list_display = ('title',)			# what fields display in tables

admin.site.register(Genre, GenreAdmin)


class DirectorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')

admin.site.register(Director, DirectorAdmin)


class ActorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')	

admin.site.register(Actor, ActorAdmin)





def export_xls(modeladmin, request, queryset):
	response = HttpResponse()
	response['Content-Disposition'] = 'attachment; filename=produkty.xls'
	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet("Movies")
	row_num = 0
	columns = [
		(u"ID", 2000),
		(u"Title", 6000),
		(u"Genres", 8000),
		(u"Directors", 3000),
	]
	header_style = xlwt.XFStyle()
	header_style.font.bold = True
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num][0], header_style)
		# ustawia szerokość kolumny
		ws.col(col_num).width = columns[col_num][1]

	# tekst w odpowiednich komórkach będzie zawijany
	text_style = xlwt.XFStyle()
	text_style.alignment.wrap = 1

	# specjalny styl numeryczny z dwoma miejscami po przecinku
	price_style = xlwt.XFStyle()
	price_style.num_format_str = '0.00'

	styles = [text_style, text_style, text_style, price_style]

	for obj in queryset.order_by('pk'):
		row_num += 1
		row = [
			obj.pk,
			obj.title,
			', '.join([i.title for i in obj.genres.all()]),
			', '.join([str(i) for i in obj.directors.all()])
		]

		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], styles[col_num])

	wb.save(response)
	return response

export_xls.short_description = u"Eksportuj do pliku XLS"


class PhotoFilter(admin.SimpleListFilter):
	# Czytelny tytuł, który zostanie wyświetlony po prawej
	# stronie panelu administracyjnego, nad opcjami filtrowania.
	title = _(u'Photos')
	# Parametr dla filtru, który zostanie użyty w zapytaniu URL.
	parameter_name = 'photos'

	def lookups(self, request, model_admin):
		"""
		Zwraca listę krotek. Pierwszy element w każdej
		krotce jest zakodowaną wartością opcji, która
		pojawi się w zapytaniu URL. Drugi element to
		czytelna nazwa opcji, która pojawi się na pasku
		po prawej stronie.
		"""
		return (
			('0', _(u'Nie ma zdjęć')),
			('1', _(u'Ma jedno zdjęcie')),
			('2+', _(u'Ma więcej niż jedno zdjęcie')),
		)

	def queryset(self, request, queryset):
		"""
		Zwraca przefiltrowany zbiór obiektów na podstawie
		wartości dostarczonej w łańcuchu zapytania, który
		można pobrać przy użyciu konstrukcji self.value().
		"""
		queryset = queryset.annotate(num_photos=models.Count('moviephoto'))
		if self.value() == '0':
			return queryset.filter(num_photos=0)
		if self.value() == '1':
			return queryset.filter(num_photos=1)
		if self.value() == '2+':
			return queryset.filter(num_photos__gte=2)


class MoviePhotoInline(admin.StackedInline):
	model = MoviePhoto
	extra = 0


class MovieAdmin(admin.ModelAdmin):
	list_display = ('title', 'rating', 'get_photo')
	list_editable = ('rating',)
	list_filter = [PhotoFilter]

	inlines = [MoviePhotoInline]
	actions = [export_xls]

	def get_photo(self, obj):
		movie_photo = obj.moviephoto_set.first()
		if movie_photo:
			return u'<a href="{0}" target="_blank"><img src="{0}" alt="" width="100"/></a>'.format(
				movie_photo.photo.url)
		

	get_photo.short_description = u'First photo'
	get_photo.allow_tags = True

admin.site.register(Movie, MovieAdmin)





# Zmienianie ustawienia administracyjnych aplikacji django.contrib.auth na własne ustawienia administracyjne
class UserAdminExtended(UserAdmin):
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined', 'last_login')
	list_filter = ('is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
	ordering = ('last_name', 'first_name', 'username')
	save_on_top = True


class GroupAdminExtended(GroupAdmin):
	list_display = ("__str__", "display_users")
	save_on_top = True

	def display_users(self, obj):
		links = []
		for user in obj.user_set.all():
			links.append(
				"""<a href="/admin/auth/user/{0}/" target="_blank">{1}</a>""".format(
				user.id,
				(u"{0} {1}".format(user.first_name, user.last_name)).strip() or
				user.username
				)
			)
		return u"<br />".join(links)

	display_users.allow_tags = True
	display_users.short_description = _(u"Users")

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdminExtended)
admin.site.register(Group, GroupAdminExtended)
