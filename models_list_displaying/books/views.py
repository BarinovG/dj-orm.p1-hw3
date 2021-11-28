from django.shortcuts import render, redirect, reverse
from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()

    context = {'books': books}
    return render(request, template, context)


def books_by_date_view(request, pub_date):
    home_page = f"<a href={reverse('books')}>Full_list</a>"
    template = 'books/books_by_date.html'
    books = Book.objects.filter(pub_date=pub_date)
    dates = Book.objects.values_list('pub_date', flat=True).distinct()

    if len(dates) > 0:
        for idx, date in enumerate(dates):
            if date == pub_date:
                used_index = idx

    prev_date = None
    next_date = None
    if used_index > 0:
        prev_date = dates[used_index - 1]
    if used_index < len(dates) - 1:
        next_date = dates[used_index + 1]

    context = {
        'pub_date': pub_date,
        'books': books,
        'prev_date': prev_date,
        'next_date': next_date,
        # '',
    }
    return render(request, template, context)
