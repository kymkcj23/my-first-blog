
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('여기는 정아음의 홈 페이지')
