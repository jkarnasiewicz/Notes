# -*- coding: utf-8 -*-

# Fluent python
# check import order in metaprograming chapter
# 717 python jargon
# raise from lambda !

# ML/25
# JS/124

import django
import matplotlib
import pandas
import os, sys
from pprint import pprint
pprint(dir(os))
print(os.getcwd())

with open('data_with_headers.csv', 'wt', encoding='utf-8') as f:
	x = range(-100, 101)
	y = (i**3 - i**2 + 7 for i in x)
	z = (i**2 + 5*i + 6 for i in x)
	t = (i**4 for i in x)
	f.write('{},{}, {}, {}\n'.format('X', 'Y', 'Z', 'T'))
	for row in zip(x, y, z, t):
		f.write('{}, {}, {}, {}\n'.format(row[0], row[1], row[2], row[3]))

# print(__builtins__)