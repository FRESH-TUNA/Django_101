from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index, name="index")
]

#현재폴더는 .
#현재폴더의 element는 .element로 나타낸다.