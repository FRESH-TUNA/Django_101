from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index, name="index"),
    path('create', views.create, name="create"),
    path('<int:pk>/update', views.update, name="update"),
    path('<int:pk>/delete', views.delete, name="delete"),
]

#현재폴더는 .
#현재폴더의 element는 .element로 나타낸다.