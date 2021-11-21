from django.shortcuts import render, redirect
from django.http import Http404
from phones.models import Phone

SORT_MAP = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price',
}


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort:
        phones = phones.order_by(SORT_MAP[sort])
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone = Phone.objects.get(slug=slug)
    except:
        raise Http404("'Don't have that model")
    context = {
        'phone': phone
    }
    return render(request, template, context)
