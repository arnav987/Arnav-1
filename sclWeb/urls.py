from django.urls import path
from . import views

urlpatterns = [
    path("", views.login),
    path("logform", views.logform),
    path("reg", views.reg),
    path("regForm", views.regForm),
]