# Simple Python server
# =================================
hostname $ python -m http.server 9000


# Status code:
# ===========================
# 2XX Success
200 Ok
201 Created

# 3XX Redirection
301 Moved Permanently (Trwale przeniesiony – żądany zasób zmienił swój URI i w przyszłości zasób powinien być szukany pod wskazanym nowym adresem)
302 Found (Znaleziono – żądany zasób jest chwilowo dostępny pod innym adresem a przyszłe odwołania do zasobu powinny być kierowane pod adres pierwotny)

304 Not Modified

# 4XX Client Error
400 Bad Request (Nieprawidłowe zapytanie – żądanie nie może być obsłużone przez serwer z powodu błędnej składni zapytania)
403 Forbidden (Zabroniony – serwer zrozumiał zapytanie lecz konfiguracja bezpieczeństwa zabrania mu zwrócić żądany zasób)
404 Not Found

# 5XX Server Error
500 Internal Server Error


# DNS:
# ===========================
Domain Name System


# Protocol(protokół):
# ===========================
Http, Htpps

# apache
# =================================
<VirtualHost 10.26.27.25:80>
    ServerName iel-dev.e-science.pl:80

    ErrorLog logs/iel_error_log
    TransferLog logs/iel_access_log
    LogLevel warn

    AddDefaultCharset utf-8
    SetEnv LANG pl_PL.UTF-8


    DocumentRoot /var/www
    Alias /robots.txt /usr/local/www/docs/robots.txt
    #Alias /favicon.ico /var/www/wsgi/static/images/favicon.ico

    <Directory /var/www/wsgi/static/IEL>
    Order deny,allow
    Allow from all
    </Directory>

    <Directory /var/www/wsgi/media>
    Order deny,allow
    Allow from all
    </Directory>

    WSGIDaemonProcess iel_escience user=iel group=iel processes=2 threads=15 display-name=%{GROUP}
    WSGIProcessGroup iel_escience
    WSGIScriptAlias / /var/www/wsgi/scripts/iel.wsgi

    <Directory /var/www/wsgi/scripts>
    Order deny,allow
    Allow from all
    </Directory>

    #50 MB
    LimitRequestBody 52428800
</VirtualHost>


# wsgi
# ========================================== 
# cat /var/www/wsgi/scripts/iel.wsgi
import os, sys

sys.path.insert(0, '/home/iel')
sys.path.insert(1, '/home/iel/LKE')
sys.path.insert(2, '/home/iel/LKE/LKE')
os.environ['DJANGO_SETTINGS_MODULE'] = 'LKE.settings'



import site
site.addsitedir('/home/iel/pythonIEL/lib/python2.7/site-packages')

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()


# To Do
email = email_base@domain.extension
