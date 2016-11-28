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

=========================

VPN
/etc/openvpn/
/etc/init.d/openvpn start

=========================

SUPERVISOR

sudo supervisord -c /etc/supervisor/supervisord.conf
sudo supervisorctl -c /etc/supervisor/supervisord.conf

sudo supervisorctl reread
sudo supervisorctl update

=========================

DJANGO

sudo less /var/log/syslog
tail -f /var/log/syslog

=========================

NGINX

sudo /etc/init.d/nginx restart
reload/start/stop

Nginx password
Create the Password File Using the OpenSSL Utilities
sudo sh -c "echo -n 'sammy:' >> /etc/nginx/.htpasswd"

Next, add an encrypted password entry for the username by typing:
sudo sh -c "openssl passwd -apr1 [password] >> /etc/nginx/.htpasswd"

=========================

GUNICORN
(lokalnie) gunicorn eds.wsgi:application --bind 127.0.0.1:8004 --log-level=debug

gunicorn ... --preload

/home/ubuntu/beta.log

stdout_logfile = /var/log/supervisor/gunicorn_beta.log
stderr_logfile = /var/log/supervisor/gunicorn_beta_error.log


=========================

CELERY
(lokalnie) python manage.py celery worker -B -c 1 --loglevel=INFO

./manage.py celery status
shell

LOGFILE=/var/log/apps/celery_beta.log

stdout_logfile = /var/log/supervisor/celery_beta.log
stderr_logfile = /var/log/supervisor/celery_beta_error.log

=========================

REDIS
:6379

/etc/redis/redis.conf

First, I flush all keys stored in redis in order to remove old cache entries (never do this in production as this removes all data from redis):
redis-cli FLUSHALL

Then activate caching in my application, and see what redis does:
redis-cli MONITOR

redis-cli INFO | grep ^db

=========================

MEMCACHED
:11211

memcached -vv
/etc/init.d/memcached restart

=========================

ELASTICSEARCH
:9200

curl -X GET 'http://localhost:9200'
http://localhost:9200/haystack_beta

wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb http://packages.elastic.co/elasticsearch/2.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list
sudo apt-get update
sudo apt-get install elasticsearch
sudo update-rc.d elasticsearch defaults 95 10
sudo /etc/init.d/elasticsearch start
