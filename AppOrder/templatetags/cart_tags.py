from AppShop.models import Category
from django import template
from django.template.loader import get_template
from AppOrder.models import Cart
from AppLogin.models import User


register = template.Library()


@register.filter
def cart_items(user):
    return Cart.objects.filter(user=user, purchased=False).count()


@register.simple_tag
def get_categories():
    cats = Category.objects.all()
    return cats



# template_name = get_template('navbar.html')
# register.inclusion_tag(template_name)(get_categories)