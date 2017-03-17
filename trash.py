# -*- coding: utf-8 -*-

# Fluent python
# check import order in metaprograming chapter
# 717 python jargon
# raise from lambda !

# ML/25
# JS/124

# ?! - annotation

# import django
import numpy as np
# import matplotlib
# import pandas
# import os, sys
from pprint import pprint
import math


# with open('data_with_headers.csv', 'wt', encoding='utf-8') as f:
# 	x = np.arange(-5, 5, 0.1)
# 	y = (i**3 - i**2 - 7 for i in x)
# 	z = (i**2 + 5*i + 6 for i in x)
# 	t = (10*math.sin(i) for i in x)
# 	u = (-i - 20 for i in x)
# 	v = (math.sqrt(abs(i)) - 20 for i in x)
# 	f.write('{},{}, {}, {}, {}, {}\n'.format('X', 'Y', 'Z', 'T', 'U', 'V'))
# 	for row in zip(x, y, z, t, u, v):
# 		f.write('{}, {}, {}, {}, {}, {}\n'.format(row[0], row[1], row[2], row[3], row[4], row[5]))

print(np.arange(1, 2, 10))
