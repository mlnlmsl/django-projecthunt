from django.urls import path
from . import views

# url patterns for the user
urlpatterns = [
    path('', views.index)
]
