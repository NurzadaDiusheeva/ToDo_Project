from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, ToMeet

def homework(request):
    return render(request, "index.html")

def todo_list(request):
    return render(request, "homework.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def meeting_list(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, "meeting.html", {"tomeet_list": tomeet_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_tomeet(request):
    form = request.POST
    text = form["tomeet_text"]
    tomeet = ToMeet(person=text)
    tomeet.save()
    return redirect(meeting_list)