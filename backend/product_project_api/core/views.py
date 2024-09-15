from django.shortcuts import render
from django.middleware.csrf import get_token

from .forms import ProductForm


def index(request):
    """
    Представление для отображения главной страницы.
    """

    template = 'index.html'
    form = ProductForm(request.POST or None)
    csrf_token = get_token(request)
    if form.is_valid():
        form.save()
    return render(request, template, {'form': form, 'csrf_token': csrf_token})
