from django.contrib import admin
from django.urls import path
from . import views                           # !!!

urlpatterns = [
    path('', views.homepage, name='home'),    # !!!
    path('admin/', admin.site.urls),
]
# mysite/views.py
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('여기는 홈 페이지')