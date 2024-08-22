from django.urls import path
from .views import *
urlpatterns = [
    path('user',Users.as_view()),
    path('login',LoginView.as_view()),
]