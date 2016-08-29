# -*- coding: UTF-8 -*-
"""
Template tags for Django
"""
import logging

from django import template

register = template.Library()

logger = logging.getLogger('ratings')


class RatingStarsNode(template.Node):

    def __init__(self, obj, class_name=None):
        self.obj = obj
        self.class_name = class_name

    def render(self, context):
        rating = int(template.resolve_variable(self.obj, context))
        result = []
        result.append("""<span class="rating-stars %s">""" % (self.class_name
                                                              or ''))
        for r in range(1, 6):
            if r <= int(rating):
                result.append('<i star="%d" class="icon-star"></i>' % r)
            elif r - rating <= 0.5:
                result.append('<i star="%d" class="icon-star-half"></i>' % r)
            else:
                result.append('<i star="%d" class="icon-star empty"></i>' % r)
        result.append("</span>")
        return ''.join(result)

@register.tag(name='rating_stars')
def do_rating_stars(parser, token):
    """
    Example usage:
        {% rating_stars vote %}
    """
    bits = token.contents.split()
    if len(bits) == 3:
        return RatingStarsNode(bits[1], class_name=bits[2])
    if len(bits) == 2:
        return RatingStarsNode(bits[1])
    raise template.TemplateSyntaxError("'%s' tag takes exactly one argument"
                                       % bits[0])
