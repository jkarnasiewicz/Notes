def silnia(n):
	a = 1
	if n==0 or n==1:
		return 1
	while n>0:
		a = a*n
		n = n-1
	return a

def silnia1(n):
 if n==0:
  return 1
 for a in range(1,n):
  n = a*n
 return n	

def silnia2(n):
	return n*silnia2(n-1) if n>1 else 1

print(silnia(6))
print(silnia1(1))
print(silnia2(5))



#Rzozklad liczby na czynniki pierwsze
def rozklad(n):
   L = []
   A = []	
   for i in range(2,n):
      while n%i == 0:
         L.append(i)
         n = n/i
      if L.count(i) == 0:
         continue
      A.append(L.count(i))
   B = [x for x in set(L)]
   return [(B[i],A[i]) for i in range(len(B))], L

print(rozklad(24))



#Reverse binary number
a = [a for a in bin(47)]
b = a.index('b')
c = a[b+1:]
c.reverse()
a[b+1:] = c
d = ''.join(a)
print(int(d,2))



#Creating Folders and String Formating
import os   
for x in range(1,7):
 path = ('D:\Filmy\Przyklad\Season {}'.format(x))
 os.makedirs(path)


#Count
c = 'abcdeabcdabcaba'
def licz(x):
  d = {}
  for i in x:
    if i not in d:
      d[i] = 1
    else:
      d[i] += 1
  return d  

print(sorted(licz(c).items(), key = lambda s: s[1], reverse = True)[:3])
 



#Host and IP 
import socket
myname = socket.getfqdn(socket.gethostname( ))
myaddr = socket.gethostbyname(myname)
print("Host:", myname, "IP:", myaddr)



#From Tutorial...
import urllib.request
from xml.etree.ElementTree import parse

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()

doc = parse('rt22.xml')
for bus in doc.findall('bus'):
	d = bus.findtext('d')
	lat = float(bus.findtext('lat'))

print(d, "\n", lat)



#Finding url's in txt file and writing them into file or showing them in webbrowser
import webbrowser
import re
a = open('ZakladkiFireFox.txt')
data = a.read()
url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)
b = open('Zakladki1.txt','w')
for x in url:
#	webbrowser.open_new_tab(x)
 b.write(x + "\n")
# print(x)
b.close()
