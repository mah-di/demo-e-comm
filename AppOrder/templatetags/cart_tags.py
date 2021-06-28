from django import template
from AppOrder.models import Cart


register = template.Library()


@register.filter
def cart_items(user):
    return Cart.objects.filter(user=user, purchased=False).count()