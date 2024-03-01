from django import template
from django.utils.safestring import mark_safe

register = template.Library()

#le tags pour afficher maximun arg mot sur le template pour un element de type chaine de caractere
@register.filter
def truncatewords(value, arg):
    words = value.split()[:arg]
    return mark_safe(' '.join(words))