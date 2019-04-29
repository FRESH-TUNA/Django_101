from django.shortcuts import render

# Create your views here.
# render한결과를 반드시 return 하자
def index(request):
    return render(request, "PhoneBook/index.html")