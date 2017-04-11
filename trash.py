# -*- coding: utf-8 -*-

# Fluent python
# check import order in metaprograming chapter
# 717 python jargon
# raise from lambda !

# ML/25
# JS/208

# Testing JavaScript:
# jsHint
# QUnit
# Modernizr.load - feature detection(e.g. browser)
# math.js/accounting.js/numbers.js - mathematics
# Minify Your Library



# End
# unittest module
# regexp



# ?! - annotation
# Tests
# try to not create database instances(no save()), try to focuse on full_clean()



# aplikacja 'zapytania'

# self.assertIn('__all__', form.errors)
# self.assertIn('Please correct min, max or step value.', form.errors['__all__'])
# Czy jest sens testować dosłowne wiaomości błędów?

# django forms
# ?! In cases when field validators detect error that clean_field is omitted
# błąd(niścisłość) w dokumentacji? 

# czy jest mozliwe dodać dodatkowe informacje podczas wysyłania HttpResponse z plikiem do ściągnięcia np. reset formularza?

# jak prawidłowo 'renderować' pliki javascript (var name = {% var %}; => but you can replace that from js)?

# chcialbym przyspieszyc testy, poprzez uzycie mockow, czy to ma sens w przypadku gdy testujemy zewnetrzne zrodlo?
# Mockowe testy przejda szybko i pomyslnie lecz aplikacja bedzie chodzic blednie



# RAZORHILL MUSIC
# Stop making scv-s from one base at 22

import numpy as np
# from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import style
# style.use("ggplot")

# centers = [[1, 1, 1], [5, 5, 5], [3, 10, 10]]

X, _ = make_blobs(n_samples = 20, centers = 3, cluster_std = 1.5, n_features=2, shuffle=False, center_box=(-100, 100))
print(X, _)

# ms = MeanShift()
# ms.fit(X)
# labels = ms.labels_
# cluster_centers = ms.cluster_centers_

# # print(cluster_centers)
# n_clusters_ = len(np.unique(labels))
# # print("Number of estimated clusters:", n_clusters_)

# colors = 10*['r','g','b','c','k','y','m']
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# for i in range(len(X)):
#     ax.scatter(X[i][0], X[i][1], c=colors[labels[i]], marker='o')

# ax.scatter(cluster_centers[:,0],cluster_centers[:,1],
#             marker="x",color='k', s=150, linewidths = 5, zorder=10)

# plt.show()
# from matplotlib import cm
# colors = cm.plasma(np.linspace(0.0, 1.0, 3))
# print(colors)

# import matplotlib
# c = matplotlib.colors.to_rgba(colors[0], alpha=None)
# c = [255*i for i in c]
# print(c)