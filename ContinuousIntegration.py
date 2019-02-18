# Ciągłe procesy programistyczne (Jenkins, Buildbot, Travis CI+GitHub, GitLab CI)
1. ciągła integracja oprogramowania (CI - continuous integration, ciągła budowa/kompilacja/automatyczne testowanie aplikacji)
	usługi dostępne w internecie: GitHub, Bitbucket
	utrzymywane na własnych serwerach: GitLab
	- testowanie kazdej zmiany
	- macierze testowe (przyklady parametrów: rózne systemy operacyjne, bazy danych, wersje uslug wspierajacych, systemy plików)
	np. konkretna wersja django wspiera konkretne wersje pythona


	artefakty - pliki powstałe podczas procesu budowy/komilacji aplikacji (np. dla języków kompilowanych, są już gotowe do dostarczenia)
2. ciągłe dostarczanie oprogramowania (continuous delivery)
	glownym celem jest wydawanie oprogramowania w bardzo krotkich cyklach - przyrostowe dostarczanie usprawnien i nowych funkcjonalnosci
3. ciągłe wdrażanie oprogramowania (continuous deployment)
	wdorzenie kodu odbywa sie za pomoca systemu ciaglej intregracji - zachodzi automatycznie i bezwarunkowo za kazdym razem gdy nowe zmiany
	pojawia sie na galezi glownej kodu

# Regresja
blad ktory byl wczesniej rozwiazany, lub taki ktory dotyczy funkcjonalnosci dzialajacych dotychczas bezproblemowo

# Master and Slave
Master - server sterowniczy, Slave - serwer wykonawczy

Problemy/Częste pułapki CI:
zbyt skomplikowane strategie działań => testuj wszystko, testuj zawsze
zbyt długie czasy testowania => znaleźć wąski gardła całego procesu, zoptymalizować, podzielić procedurę testową na mniejsze części i dokonać
								zrównoleglenia wymiana sprzętu na szybszy, zmiana ogólnej architektury projektu
zewnętrzne definicje zadań(antywzorzec) => najelpiej jeśli definicja procedury testowej jest przechowywana wraz
										   z testowanym kodem wewnątrz jego repozytorium
brak izolacji => środowisko testowe powinno być jak najbardziej zblizone do produkcyjnego,
				 zapewnienie odpowiedniej izolacji na poziomie systemowym(nie tylko wirtualne srodowisko dla pythona)
