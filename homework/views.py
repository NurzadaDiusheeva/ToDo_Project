from django.http import HttpResponse
from django.shortcuts import render

def homework(request):
    return render(request, "index.html")

def todo_list(request):
    return render(request, "homework.html")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("Test 2  page")
