# Itertools
# imap, ireduce, ifilter i izip === map, reduce, filter, zip (python 3)
# islice - umożliwia podział potencjalnie nieskończonego generatora.
# chain - laczy w łańcuch wiele generatorów.
# takewhile - dodaje warunek, który powoduje zakończenie działania generatora.
# cycle - rzez ciągłe powtarzanie skończonego generatora powoduje, że staje się on nieskończony.

# numpy.show_config()
# numpy.arange()
# numpy.array()

# Django - Najlepsze receptury
# To Do
# Tworzenie domieszek do modeli do obsługi relacji generycznych (46)
# Wysyłanie obrazów na serwer i tworzenie miniatur obrazow (66)





# 0. pep-8 (http://legacy.python.org/dev/peps/pep-0008/)
# 1. Tworzenie domieszek do modeli do obsługi metaznaczników i url-ow (43)
# 2. Dynamiczne ustawianie wartości zmiennej STATIC_URL dla użytkowników systemu Git
# 3. Tworzenie i dołączanie ustawień lokalnych (ustawienia lokalne, a ustwienia produkcyjne)(settings-local.py)
# 4. Konfigurację JavaScript - dobrym pomysłem jest dodanie dynamicznie generowanego pliku
# 	 konfiguracyjnego do szablonu bazowego
# 5. Paginator, infinitive scroll, boostrap modals
# 5. Kodowanie bazy danych (utf-8)
# 6. Tworzenie pliku z informacjami o ignorowanych zasobach w systemie Git (.gitignore)
# 7. Usuwanie skompilowanych plików Pythona (.bash_profile)
# 8. Base models (e.g. for Mixins, base_models.py)





# W systemie Django wyróżnia się trzy typy dziedziczenia modeli: abstrakcyjne klasy bazowe (Abstract base classes),
# dziedziczenie wielotabelowe (Multi-table inheritance) oraz modele proxy (Proxy models).

# Domieszki(Mixins) modeli są abstrakcyjnymi klasami modeli z określonymi polami, własnościami i metodami.
# Mixins encourage code reuse. A mixin can also be viewed as an interface with implemented methods.

# Each model corresponds to its own database table and can be queried and created individually.
# The inheritance relationship introduces links between the child model and each of its parents
# (via an automatically-created OneToOneField)

# Creating a proxy for the original model. You can create, delete and update instances of the proxy model
# and all the data will be saved as if you were using the original (non-proxied) model

class Meta:
	verbose_name = _(u"Pomysł")
	verbose_name_plural = _(u"Pomysły")
	abstract = True
	proxy = True





# Przekazywanie całego reqesta do formularza
# forms.py
class MessageForm(forms.Form):
	# ...
	def __init__(self, request, *args, **kwargs):
		super(MessageForm, self).__init__(*args, **kwargs)
		self.request = request					# mozemy z niej skorzystać później
		self.fields['recipient'].queryset = self.fields['recipient'].queryset.exclude(pk=request.user.pk)

# views.py
@login_required
def message_to_user(request):
	if request.method == "POST":
		form = MessageForm(request, data=request.POST)
		if form.is_valid():
			# ...
			return redirect("message_to_user_done")
	else:
		form = MessageForm(request)
	return render(request, "email_messages/message_to_user.html", { 'form': form })



# Try Django 1.9
# 26 - Bootstrap(html offset),
# 27 - Pagination
# 30 - social share links
# 34 - using facebook comments
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eds.settings.dev")

# Imported modules
import sys
sys.modules

# Import loops
code refactor => create additional file and put there messy code(functions, classes)

# Books
Even Faster Web Sites: Performance Best Practices for Web Developers

# Nginx, blokady dla uzytkownikow, ale musi wpuszczać nas(po IP)