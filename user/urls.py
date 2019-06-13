from django.urls import path
from . import views

# url patterns for the user
urlpatterns = [
    path('', views.index),
    path('user/login', views.login),
    path('/dashoard', views.dashboard, name="dashboard"),
    path('register/', views.register, name="register")
]
