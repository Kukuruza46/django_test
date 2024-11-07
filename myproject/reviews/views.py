from django.shortcuts import render
from django.http import HttpResponse
from .models import Review

def home(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/home.html', {'reviews': reviews})
