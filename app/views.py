from django.shortcuts import render
from django.conf import settings
from .models import *

# Create your views here.


def home_page(request):
    images = Images.objects.get(id=1)
    quotes = Quotes.objects.all()
    trend_books = Trend_books.objects.all()
    contact = Contact.objects.all()
    book1 = Quotes.objects.last()
    book2 = Quotes.objects.first()
    context = {
        "images": images,
        "quotes": quotes,
        "trend_books": trend_books,
        "contact": contact,
        "book1": book1,
        "book2": book2,
    }
    if request.method == "POST":
        email = request.POST["email"]
        full_name = request.POST["full_name"]
        models.Contact.objects.create(email=email, full_name=full_name)
    return render(request, "index.html", context)
