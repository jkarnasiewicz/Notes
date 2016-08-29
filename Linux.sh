# General
id                                  # information about user and users grups
uname -a 							# generall information about system
clear
sudo reboot
sudo shutdown
sudo kill 7831



# Information
top									# memory usage
htop								# memory usage/task manager
ps -ef -f							# display all processes
ps -f -u user_name 					# show processes by user
ps -f  -p 3150,7298,6544			# show processes by id
ps -ef | grep apache 				# show processes by name
ps aux | grep supervisor

more file_name						# show content of the file
lsof                                # list of open/working files and aplications that uses them
pwd 								# print working directory
man nmap                           	# manual do nmap-a
cat /proc/meminfo                   # memory info
cat /proc/cpuinfo                   # cpu info

apt-cache pkgnames | less           # available packages in the system
apt-cache pkgnames fire | less      # packages starting with “fire”
apt-cache show firefox
apt-cache stats



# cd
cd "LIGiG(test)"/
cd LIGiG\(test\)/



# Search
ctrl + r 							# search in bash history
find /home/... -name file_name		# find file/application
find . -name '*.py'|xargs flake8	# find every python file and run flake8 on it
find . -name \*.pyc -delete			# delete every .pyc file
which name 							# path of the installed application



# Copy
cp ../SPO/.gitreview ./								# cp from to
scp pliki.py karnasiewicz@nereid.wcss.wroc.pl:~/ 	# secure copy
scp karnasiewicz@nereid.wcss.wroc.pl:~/plik.pdf ~/Pobrane/

scp -r user@your.server.example.com:/path/to/foo /home/user/Desktop/ 	# recursively copy entire directories



# Move/Cut/Rename
mv /home/you/somefile.txt /tmp/newlocation.txt



# Create
mkdir folder_name									# create folder
touch file_name.py 									# create file
cat > file_name



# Remove
rm -r folder_name									# remove folder whith files



# apt-get
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install firfeox
# apt-get upgrade .deb packages
# Instead of using dpkg, which is a low level package manager, youd be better off using apt.
# To install the .deb files using apt, copy them to the apt cache - sudo cp *.deb /var/cache/apt/archives/
# and then just do the regular apt-get upgrade.
sudo apt-get update nginx

sudo apt-get install python-dev gfortran libopenblas-dev liblapack-dev libfreetype6-dev libldap2-dev libsasl2-dev libpng-dev
sudo apt-get build-dep python-lxml
sudo apt-get install git
sudo apt-get install gitk/gitg

sudo apt-get remove packagename
sudo apt-get remove --purge packagename
apt-get autoremove



# dpkg
sudo dpkg -i package_name				# install or upgrade package
dpkg -R directory-name 					# install all packages recursively from directory
dpkg -r package_name					# remove/delete an installed package except configuration files
dpkg -P package_name					# remove/delete everything including configuration files

dpkg -L package_name 					# find out files are provided by the installed package i.e. list where files were installed
dpkg -l									# list of installed packages
dpkg -l package_name					# list individual installed packages, along with package version and short description

dpkg -s package_name					# is package installed?
dpkg -c .deb_package 					# list files provided (or owned) by the package i.e. List all files inside debian .deb package file,
# 										  very useful to find where files would be installed



# pip
sudo apt-get install python-pip
sudo easy_install pip

pip install pip --upgrade
pip install Distribute --upgrade
pip install numpy
pip install scipy
pip install Django==1.9
pip install flake8

pip uninstall django

# wheel files
pip install some-package.whl

# pip Pillow
pip install Pillow
sudo apt-get install libjpeg-dev
# reinstall pillow
pip install --no-cache-dir -I pillow

pip install MySQL-python



# virtualenv
sudo pip install virtualenv
virtualenv /nazwa_folderu
source /bin/activate



# connection
ping 156.17.181.95
host pwr.edu.pl
traceroute 212.77.100.101          					# sprawdzenie drogi sygnalu/requesta (pokazuje wszystkie wezly/hub-s)
telnet 156.17.181.95 1443                           # conection information

sudo apt-get install nmap
nmap eridani.wcss.pl               					# sprawdzenie dostepnosci wszystkich portow
nmap -p 22 eridani.wcss.pl         					# sprawdzenie nmap-em portu 22 nmap na eridani.wcss.pl
nmap -T4 156.17.181.95 -PN               			# searching ports(info about all ports). T4 - spowolnienie odpytywan(zbyt duzo zapytan na sekunde z tego samego miejsca)
nmap -T4 -p 1433 156.17.181.95 -PN               	# info about port 1433

tsql -H 156.17.181.95 -p 1433 -U 'SpinLab' -P 'gApTv#91$D' -D 'MaGDA' # -h host -p port -U user -P password
tsql -S sqlserver -U 'SpinLab' -P 'gApTv#91$D' -D 'MaGDA'



# format device
df
sudo umount /dev/sdb1
sudo mkfs.vfat -n 'name' -I /dev/sdb1
sudo apt-get install gparted



# Latex
apt-get install texlive-full						# texlive-xetex



# crontab(/etc/crontab)
crontab -e                                          # User cron
sudo service cron restart							# ... reload
sudo vim /etc/crontab                               # Administartor level

crontab --> run_cron.sh --> python manage.py MyCommand

# run_cron.sh file

#!/bin/bash
cd $HOME/Dokumenty/LIGiG/
source $HOME/Dokumenty/Ve-LIGiG/bin/activate
python manage.py update



# Cifs (dysk sieciowy)
sudo apt-get install cifs-utils
sudo groupadd samba
sudo adduser user samba
sudo visudo
sudo mount -t cifs //dysk.e-sci.e-science.pl/samba ~/mnt -o username=jacek.karnasiewicz
sudo umount ~/mnt



# ssh(secure shell) keys
~/.ssh/id_rsa                           # Key private part
~/.ssh/id_rsa.pub                       # Key public part



# logs info
ssh karnasiewicz@nereid.wcss.wroc.pl
ssh root@dspace.dev.kdm.wcss.pl                 # connect to server
su -l dspace                                    # Login as dspace
tail -f dspace/log/dspace.log.2015-06-01        # display latest logs



# sshfs
sshfs jacek.karnasiewicz@sshdysk.e-science.pl:/spinlab ~/mnt/
sshfs karnasiewicz.ligig@sshdysk.e-science.pl:/gnssandmeteo ~/mnt/
fusermount -u ~/mnt/



# application
vim
nano
pgadmin3
pidgin
ip a # inet



# To Do
.bash_profile
sudo chown -R jacek.karnasiewicz:jacek.karnasiewicz /home/jacek.karnasiewicz


# MySQL
mysql -u root -p
mysql -u root -p eds4 < file_name.sql
sudo /etc/init.d/mysql restart


# Database - change database collation
ALTER DATABASE <database_name> CHARACTER SET utf8 COLLATE utf8_unicode_ci;
# Table
ALTER TABLE <table_name> CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
# Column
ALTER TABLE <table_name> MODIFY <column_name> VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci;

# Change root password (from 'abc' to '123456')
mysqladmin -u root -p'abc' password '123456'

sudo apt-get install mysql-server
sudo apt-get install libmysqlclient-dev

# Symbolic Link
sudo ln -s /usr/lib/libgeos_c.so /usr/local/lib/

sudo apt-get install geos-config

hostname -f

#/home/myproject/commands/cleanup.bsh
su myproject "-c source /home/myproject/bin/activate &&
	cd /home/myproject/project/myproject/ && python manage.py clearsessions"
# Następnie zdefiniuj uprawnienia do wykonywania tego nowego pliku:
(myproject)myproject@server$ chmod +x cleanup.bsh

#~/db_backups/backupdb.bsh
#!/bin/bash
if [[ $1 = '--latest' ]]
then
today="latest"
else
today=$(date +%Y-%m-%d-%H%M)
if
mysqldump --opt -u myproject -p mypassword myproject > db_$today.sql

Poniższe polecenie zamieni skrypt w plik wykonywalny:
$ chmod +x backupdb.bsh

# h extension which stands for human readable
ls -lh

# Open terminal and execute comand
terminal -e command --noclose			# To make the terminal stay when the command exits add --noclose flag

>(create and write) vs >> (append)

# checking mysql database status(logs/errors)
mysql -u user -p
use test_xxx;
show engine innodb status;

# Remove old kernels in ubuntu (boot drive)
dpkg -l linux-* | awk '/^ii/{ print $2}' | grep -v -e `uname -r | cut -f1,2 -d"-"` | grep -e [0-9] | grep -E "(image|headers)" | xargs sudo apt-get -y purge