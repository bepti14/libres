from django.urls import path
from . import views

app_name = "appres"

urlpatterns = [
    path('', views.main, name="main"),
]