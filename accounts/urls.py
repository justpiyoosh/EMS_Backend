from accounts import views
from django.urls import path

from accounts import views

urlpatterns = [
    path('',views.login)
]