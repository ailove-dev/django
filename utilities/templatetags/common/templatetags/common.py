from django import template
from django.http import QueryDict


register = template.Library()

@register.filter
def number_format(number, args = ''):
    qd = QueryDict(args)

    decimals = int(qd['decimals']) if qd.has_key('decimals') else 0
    dec_point = str(qd['dec_point']) if qd.has_key('dec_point') else '.'
    thousands_sep = str(['thousands_sep']) if qd.has_key('thousands_sep') else ' '

    try:
        number = round(float(number), decimals)
    except ValueError:
        return number

    neg = number < 0
    integer, fractional = str(abs(number)).split('.')

    m = len(integer) % 3
    if m:
        parts = [integer[:m]]
    else:
        parts = []

    parts.extend([integer[m+t:m+t+3] for t in xrange(0, len(integer[m:]), 3)])

    if decimals:
        return '%s%s%s%s' % (
            neg and '-' or '', 
            thousands_sep.join(parts),
            dec_point, 
            fractional.ljust(decimals, '0')[:decimals]
        )
    else:
        return '%s%s' % (neg and '-' or '', thousands_sep.join(parts))

@register.filter
def replace(value, args):
    qd = QueryDict(args)
    value = unicode(value)

    if qd.has_key('from') and qd.has_key('to'):
        return value.replace(qd['from'], qd['to'])
    else:
        return value
