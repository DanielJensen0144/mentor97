from django.urls import path
from . import views

urlpatterns = [
    path('', views.browse, name="browse")
]