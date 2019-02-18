# Project Documentation
# sformalizowany proces tworzenia dokumentacji i traktowanie jej jak pełnoprawnego modułu oprogramowania,
# na równi z kodem zrodlowym

# Siedem zasad technicznego pisania
1. Pisz w dwóch krokach - skup sie w pierwszej kolejnosci na treści, a dopiero potem na stylu i schludnosci tekstu
2. Skieruj przekaz do konkretnej grupy czytelników - okresl swoich czytelnikow, jeszcze zanim zaczniesz pisać (programista, menadzer czy projektant)
3. Korzystaj z prostego stylu - dokumentacja to nie literatura piekna, dlatego utrzymuj styl tekstu tak prostym, jak to mozliwe
4. Ogranicz zakres informacji - odpowiednia organizacja materiału, segregowanie tematyczne
5. Korzystaj z realistycznych przykładów - przykłady kodu powinny być gotowe do wykorzystania bezposrednio w budowanych aplikacjach.
6. Dokumentuj lekko, ale jednoczesnie wystarczajaco
7. Korzystaj z szablonów - wymusza ujednolicenie struktury, pozwala czytelnikoom korzystac z niej w duzo szybszy i wydajniejszy sposob



# Sphinx(zbiór skryptów i rozszerzeń modułu docutils)
Automatyczne generowanie serwisu dokumentacji w formacie HTML na podstawie drzewa katalogó zawierających pliki tekstowe
w formacie reStructuredText



# Documentation Strings
def square(x):
	'''Do nothing, but document it.
	No, really, it doesn't do anything.

	Args:
		x: The number for which the square root is to be computed

	Returns:
		The square root of x.

	Raises:
		ValueError: If x is negative.
	'''
	pass

print(function.__doc__)
