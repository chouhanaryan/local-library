from django import template
register = template.Library()

@register.filter
def custom_last(value):
    last = None

    try:
        last = value[-1]
    except AssertionError:
        try:
            last = value.reverse()[0]
        except IndexError:
            pass

    return last