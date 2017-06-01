# -*- coding: UTF-8 -*-
# pip install fabric

# (myproject_env)$ fab --list

# (myproject_env)$ fab dev/staging/production deploy

# (myproject_env)$ fab dev full deploy

# Fabric functions
# local — funkcja służąca do lokalnego uruchamiania poleceń na bieżącym komputerze
# run — funkcja służąca do wykonywania poleceń jako wybrany użytkownik na zdalnym serwerze
# prompt — funkcja służąca do zadawania pytań
# get — funkcja służąca do pobierania pliku ze zdalnego serwera na komputer lokalny
# sudo — funkcja służąca do wykonywania poleceń jako użytkownik główny (lub inny)

from fabric.api import env, run, prompt, local, get, sudo
from fabric.colors import red, green
from fabric.state import output

env.environment = ""
env.full = False
output['running'] = False
PRODUCTION_HOST = "myproject.com"
PRODUCTION_USER = "myproject"


def dev():
	""" wybiera środowisko do pracy """
	env.environment = "dev"
	env.hosts = [PRODUCTION_HOST]
	env.user = PRODUCTION_USER
	print("LOCAL DEVELOPMENT ENVIRONMENT\n")

def staging():
	""" wybiera środowisko testowe """
	env.environment = "staging"
	env.hosts = ["staging.myproject.com"]
	env.user = "myproject"
	print("STAGING WEBSITE\n")

def production():
	""" wybiera środowisko produkcyjne """
	env.environment = "production"
	env.hosts = [PRODUCTION_HOST]
	env.user = PRODUCTION_USER
	print("PRODUCTION WEBSITE\n")

def full():
	""" wszystkie polecenia powinny być wykonywane bez pytań """
	env.full = True

def deploy():
	""" aktualizacje wybranego środowiska """
	if not env.environment:
		while env.environment not in ("dev", "staging", "production"):
			env.environment = prompt(red('Określ środowisko docelowe —'
				'environment (dev, staging lub production): '))
			print
	globals()["_update_%s" % env.environment]()


def _update_dev():
	""" aktualizuje środowisko rozwojowe """
	run("") # żądanie hasła
	print
	if env.full or "t" == prompt(red('Pobrać najnowszą produkcyjną bazę danych(t/n)?'), default="t"):
		print(green(" * Tworzenie zrzutu produkcyjnej bazy danych..."))
		run('cd ~/db_backups/ && ./backupdb.bsh --latest')
		print(green(" * Pobieranie zrzutu..."))
		get("~/db_backups/db_latest.sql", "tmp/db_latest.sql")
		print(green(" * Lokalne importowanie zrzutu..."))
		local('python manage.py dbshell < tmp/db_latest.sql && rm tmp/db_latest.sql')
		print
		if env.full or "t" == prompt('Wywołać polecenie prepare_dev (t/n)?', default="t"):
			print(green(" * Przygotowywanie danych..."))
			local('python manage.py prepare_dev')
	print

	if env.full or "t" == prompt(red('Pobrać media (t/n)?'), default="t"):
		print(green(" * Tworzenie archiwum mediów..."))
		run('cd ~/project/myproject/media/ && tar -cz -f ~/project/myproject/tmp/media.tar.gz *')
		print(green(" * Pobieranie archiwum..."))
		get("~/project/myproject/tmp/media.tar.gz", "tmp/media.tar.gz")
		print(green(" * Wypakowywanie i usuwanie archiwum lokalnie..."))
		for host in env.hosts:
			local('cd media/ && tar -xzf ../tmp/media.tar.gz && rm tmp/media.tar.gz')
		print(green(" * Usuwanie archiwum z serwera..."))
		run("rm ~/project/myproject/tmp/media.tar.gz")
	print

	if env.full or "t" == prompt(red('Zaktualizować kod (t/n)?'), default="t"):
		print(green(" * Aktualizowanie kodu..."))
		local('git pull')
	print

	if env.full or "t" == prompt(red('Migrować schemat bazy danych (t/n)?'), default="t"):
		print(green(" * Migrowanie schematu bazy danych..."))
		local("python manage.py migrate --no-initial-data")
		local("python manage.py syncdb")
	print


def _update_staging():
	""" aktualizuje środowisko testowe """
	run("") # żądanie hasła
	print

	if env.full or "t" == prompt(red('Ustawić ekran konserwacyjny (t/n)?'), default="t"):
		print(green(" * Ustawianie ekranu konserwacyjnego"))
		run('cd ~/public_html/ && cp .htaccess_under_construction .htaccess')
	print

	if env.full or "t" == prompt(red('Zatrzymać zadania crona (t/n)?'), default="t"):
		print(green(" * Zatrzymywanie zadań crona"))
		sudo('/etc/init.d/cron stop')
	print

	if env.full or "t" == prompt(red('Pobrać najnowszą produkcyjną bazę danych(t/n)?'), default="t"):
		print(green(" * Tworzenie zrzutu produkcyjnej bazy danych..."))
		run('cd ~/db_backups/ && ./backupdb.bsh --latest')
		print(green(" * Pobieranie zrzutu..."))
		run("scp %(user)s@%(host)s:~/db_backups/db_latest.sql ~/db_backups/db_latest.sql" % {
			'user': PRODUCTION_USER,
			'host': PRODUCTION_HOST,
	})
	print(green(" * Importowanie zrzutu lokalnie..."))
	run('cd ~/project/myproject/ && python manage.py dbshell < ~/db_backups/db_latest.sql')
	print

	if env.full or "t" == prompt(red('Wywołać polecenie prepare_staging(t/n)?'), default="t"):
		print(green(" * Przygotowywanie danych do testowania..."))
		run('cd ~/project/myproject/ && python manage.py prepare_staging')
	print

	if env.full or "t" == prompt(red('Pobrać najnowsze media (t/n)?'), default="t"):
		print(green(" * Aktualizowanie mediów..."))
		run("scp -r %(user)s@%(host)s:~/project/myproject/media/* ~/project/myproject/media/" % {
			'user': PRODUCTION_USER,
			'host': PRODUCTION_HOST,
		})
	print

	if env.full or "t" == prompt(red('Zaktualizować kod (t/n)?'), default="t"):
		print(green(" * Aktualizowanie kodu..."))
		run('cd ~/project/myproject && git pull')
	print

	if env.full or "t" == prompt(red('Pobrać pliki statyczne (t/n)?'), default="t"):
		print(green(" * Pobieranie plików statycznych..."))
		run('cd ~/project/myproject && python manage.py collectstatic --noinput')
	print

	if env.full or "t" == prompt(red('Dokonać migracji schematu bazy danych(t/n)?'), default="t"):
		print(green(" * Migrowanie schematu bazy danych..."))
		run('cd ~/project/myproject && python manage.py migrate --no-initial-data')
		run('cd ~/project/myproject && python manage.py syncdb')
	print

	if env.full or "t" == prompt(red('Uruchomić poniwnie serwer sieciowy(t/n)?'), default="t"):
		print(green(" * Ponowne uruchamianie serwera Apache"))
		sudo('/etc/init.d/apache2 graceful')
	print

	if env.full or "t" == prompt(red('Uruchomić zadania crona (t/n)?'), default="t"):
		print(green(" * Uruchamianie zadań crona"))
		sudo('/etc/init.d/cron start')
	print

	if env.full or "t" == prompt(red('Wyłączyć ekran konserwacyjny (t/n)?'), default="t"):
		print(green(" * Wyłączanie ekranu konserwacyjnego"))
		run('cd ~/public_html/ && cp .htaccess_live .htaccess')
	print


def _update_production():
	""" aktualizuje środowisko produkcyjne """
	if "t" != prompt(red('Czy na pewno chcesz zaktualizować witrynę ' + red('produkcyjną', bold=True) + ' (t/n)?'), default="n"):
		return
	run("") # żądanie hasła
	print

	if env.full or "t" == prompt(red('Włączyć ekran konserwacyjny (t/n)?'), default="t"):
		print(green(" * Włączanie ekranu konserwacyjnego"))
		run('cd ~/public_html/ && cp .htaccess_under_construction .htaccess')
	print

	if env.full or "t" == prompt(red('Zatrzymać zadania crona (t/n)?'), default="t"):
		print(green(" * Zatrzymywanie zadań crona"))
		sudo('/etc/init.d/cron stop')
	print

	if env.full or "t" == prompt(red('Wykonać kopię zapasową bazy danych(t/n)?'), default="t"):
		print(green(" * Tworzenie zrzutu bazy danych..."))
		run('cd ~/db_backups/ && ./backupdb.bsh')
	print

	if env.full or "t" == prompt(red('Zaktualizować kod (t/n)?'), default="t"):
		print(green(" * Aktualizowanie kodu..."))
		run('cd ~/project/myproject/ && git pull')
	print

	if env.full or "t" == prompt(red('Zebrać pliki statyczne (t/n)?'), default="t"):
		print(green(" * Pobieranie plików statycznych..."))
		run('cd ~/project/myproject && python manage.py collectstatic --noinput')
	print

	if env.full or "t" == prompt(red('Dokonać migracji schematu bazy danych(t/n)?'), default="t"):
		print(green(" * Migrowanie schematu bazy danych..."))
		run('cd ~/project/myproject && python manage.py migrate --no-initial-data')
		run('cd ~/project/myproject && python manage.py syncdb')
	print

	if env.full or "t" == prompt(red('Uruchomić ponownie serwer (t/n)?'), default="t"):
		print(green(" * Ponownie uruchamianie serwera Apache"))
		sudo('/etc/init.d/apache2 graceful')
	print

	if env.full or "t" == prompt(red('Włączyć zadania crona (t/n)?'), default="t"):
		print(green(" * Włączanie zadań crona"))
		sudo('/etc/init.d/cron start')
	print

	if env.full or "t" == prompt(red('Wyłączyć ekran konserwacyjny (t/n)?'), default="t"):
		print(green(" * Wyłączanie ekranu konserwacyjnego"))
		run('cd ~/public_html/ && cp .htaccess_live .htaccess')
	print
