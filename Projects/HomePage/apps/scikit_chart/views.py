import json
from random import randrange

from sklearn import linear_model
from sklearn.model_selection import train_test_split

from django.http import JsonResponse
from django.shortcuts import render


def scikit_chart(request):
	if request.method == 'POST' and request.is_ajax():
		data = json.loads(request.body)

		reg = linear_model.LinearRegression()
		X_train, x_test, Y_train, y_test = train_test_split(
			data['observations_x'],
			data['observations_y'],
			test_size=0.2,
			random_state=0)

		reg.fit([[i] for i in X_train], Y_train)

		# y = ax + b
		a = reg.coef_[0]
		b = reg.intercept_

		new_line = [[x, a*x+b] for x in [-100, 100]]
		# new_line.sort()
		# TO DO
		# accurance of the regresion_line
		# minimum points for drawing line

		return JsonResponse({'regresion_line': new_line})

	return render(request, 'scikit_chart/home.html')
