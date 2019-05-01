from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.
# render한결과를 반드시 return 하자
def index(request):
    phoneNumbers = Phonebook.objects.all()
    return render(request, "PhoneBook/index.html", {'phoneNumbers':phoneNumbers})

def inputContext(request):
    return render(request, "PhoneBook/create.html")
def create(request):
    phoneNumber = Phonebook()
    phoneNumber.name = request.GET['name']
    phoneNumber.phoneNumber = request.GET['phoneNumber']
    phoneNumber.save()
    return redirect('index')

def update(request, phoneBookId):
    phoneNumber = get_object_or_404(Phonebook, pk=phoneBookId)
    if request.method == "GET":
        return render(request, "PhoneBook/update.html", {'phoneNumber' : phoneNumber})
    else:
        phoneNumber.name = request.POST['name']
        phoneNumber.phoneNumber = request.POST['phoneNumber']
        phoneNumber.save()
        return redirect('index')

def delete(request, phoneBookId):
    phoneNumber = get_object_or_404(Phonebook, pk=phoneBookId)
    if request.method == "GET":
        return render(request, "PhoneBook/delete.html", {'phoneNumber' : phoneNumber})
    else:
        phoneNumber.delete()
        return redirect('index')

def about(request):
    return render(request, "PhoneBook/about.html")