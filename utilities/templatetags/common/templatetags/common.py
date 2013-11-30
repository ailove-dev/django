from django import template
from django.http import QueryDict


register = template.Library()


@register.filter
def number_format(number, args=''):
    qd = QueryDict(args)

    decimals = int(qd['decimals']) if 'decimals' in qd else 0
    dec_point = str(qd['dec_point']) if 'dec_point' in qd else '.'
    thousands_sep = str(['thousands_sep']) if 'thousands_sep' in qd else ' '

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

    if 'from' in qd and 'to' in qd:
        return value.replace(qd['from'], qd['to'])
    else:
        return value
