from django.shortcuts import render
from .models import *

# Create your views here.
# render한결과를 반드시 return 하자
def index(request):
    phoneNumbers = Phonebook.objects.all()
    return render(request, "PhoneBook/index.html", {'phoneNumbers':phoneNumbers})

def about(request):
    return render(request, "PhoneBook/about.html")