from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.template.exceptions import TemplateDoesNotExist


def main_view(request, menu_name):
    context = {
        'menu_name': menu_name,
    }
    try:
        return render(request, f'{menu_name}.html', context)
    except TemplateDoesNotExist:
        return HttpResponseNotFound('Нет такой страницы')