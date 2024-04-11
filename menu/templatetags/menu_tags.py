from django import template
from menu.models import MenuItem
from django.urls import reverse, NoReverseMatch
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = MenuItem.objects.filter(menu_name=menu_name, parent=None)
    except MenuItem.DoesNotExist:
        return ''

    request = context['request']
    current_path = request.path

    def render_menu_item(item):
        active_class = 'active' if current_path == item.url or (
                    item.named_url and request.resolver_match.url_name == item.named_url) else ''
        children = item.children.all()
        has_children_class = 'has-children' if children else ''

        if item.named_url:
            try:
                url = reverse(item.named_url)
            except NoReverseMatch:
                url = item.url
        else:
            url = item.url

        html = f'<li class="{active_class} {has_children_class}">'
        html += f'<a href="{url}">{item.title}</a>'

        if children:
            html += '<ul>'
            for child in children:
                html += render_menu_item(child)
            html += '</ul>'

        html += '</li>'
        return html

    menu_html = '<ul>'
    for item in menu:
        menu_html += render_menu_item(item)
    menu_html += '</ul>'

    return mark_safe(f"<h2>Menu {menu_name}</h2>{menu_html}")
