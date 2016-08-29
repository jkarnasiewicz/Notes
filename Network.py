# Book Foundations of Python Network Programming, 3rd Edition

# Network
# The layers operating below the socket() API are the following:
# Two different protocols(UDP and TCP)
TCP - The Transmission Control Protocol supports two-way conversations made of streams of
	bytes by sending (or perhaps re-sending), receiving, and re-ordering small network messages
	called packets.
UDP - 

IP - The Internet Protocol knows how to send packets between different computers.
	The Internet Protocol is a scheme for imposing a uniform system of addresses on all of the Internet-connected
	computers in the entire world and to make it possible for packets to travel from one end of the Internet to the other

The “link layer,” at the very bottom, consists of network hardware devices such as Ethernet
ports and wireless cards, which can send physical messages between directly linked
computers.



# Decoding and Encoding
Decoding is what happens when bytes are on their way into your application and you need to figure out what they
mean.
Encoding is the process of taking character strings that you are ready to present to the outside world and turning
them into bytes using one of the many encodings that digital computers use when they need to transmit or store
symbols using the bytes that are their only real currency

# Translating from the outside world of bytes to Unicode characters.
input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
input_characters = input_bytes.decode('utf-16')
print(repr(input_characters))

# Translating characters back into bytes before sending them.
output_characters = 'We copy you down, Eagle.\n'
output_bytes = output_characters.encode('utf-8')
print(repr(output_bytes))
with open('eagle.txt', 'wb') as f:
	f.write(output_bytes)


# import http.client
# import json
# from urllib.parse import quote_plus
# import pprint

# base = '/maps/api/geocode/json'

# def geocode(address):
#   path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
#   connection = http.client.HTTPConnection('maps.google.com')
#   connection.request('GET', path)
#   rawreply = connection.getresponse().read()
#   reply = json.loads(rawreply.decode('utf-8'))
#   pprint.pprint(reply)

# geocode('207 N. Defiance St, Archbold, OH')
# if __name__ == '__main__':
#   geocode('polska chojno')
