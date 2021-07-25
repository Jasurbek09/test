from django.shortcuts import render
from main.models import Book, Author, Country, Chelsea



# Create your views here.




def indexHandler(request):
    return render(request, 'index.html', {})

def booksHandler(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    countrys = Country.objects.all()
    return render(request, 'books.html', {'books': books,'authors': authors, 'countrys': countrys})

def authorsHandler(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})


def countrysHandler(request):
    countrys = Country.objects.all()
    return render(request, 'countrys.html', {'countrys': countrys})

def bookItemHandler(request, book_id):

    book = Book.objects.get(id=int(book_id))
    return render(request, 'book_item.html', {'book':book})

def countryItemHandler(request, country_id):

    country = Country.objects.get(id=int(country_id))
    return render(request, 'countryes.html', {'country':country})


def chelseasHandler(request):

    chelsea = Chelsea.objects.all()
    return render(request, 'chelseas.html', {'chelsea':chelsea})