# -*- coding: utf-8 -*-

# Fluent python
# check import order in metaprograming chapter
# 717 python jargon
# raise from lambda !

# ML/25
# JS/124

import django
import matplotlib
import os, sys
from pprint import pprint
pprint(dir(os))
print(os.getcwd())

with open('data.csv', 'wt', encoding='utf-8') as f:
	x = range(101)
	y = (i**3 - i**2 + 7 for i in x)
	for row in zip(x, y):
		f.write('{}, {}\n'.format(row[0], row[1]))
