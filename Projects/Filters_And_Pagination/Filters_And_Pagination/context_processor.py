# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve, Resolver404


def app_name(request):
    """ Context processor used to maintain app name in every template.
        Variables maintained from this processor are used to mark
        correct tab as active.
    """

    try:
        res = resolve(request.path).app_name
        return {
            'app_name': res,
        }
    except Resolver404:
        return {}
