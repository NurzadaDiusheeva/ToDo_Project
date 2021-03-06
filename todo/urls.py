"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homework.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('admin/', admin.site.urls),
    path("", homework, name="homework"),
    path("todo_list/", todo_list, name="todo_list"),
    path("test/", test, name="test"),
    path("meeting/", meeting_list, name="meeting"),
    path("add-todo", add_todo, name="add-todo"),
    path("add-tomeet", add_tomeet, name="add-tomeet"),
    path("habits/", habits, name="habits"),
    path("add-habit", add_habit, name="add-habit"),
    path("delete-todo/<id>/", delete_todo, name="delete-todo"),
    path("mark-todo/<id>/", mark_todo, name="mark-todo"),
    path("unmark-todo/<id>/", unmark_todo, name="unmark-todo"),
    path("delete-to-meet/<id>/", delete_to_meet, name="delete-to-meet"),
    path("mark-to-meet/<id>/", mark_to_meet, name="mark-to-meet"),
    path("unmark-to-meet/<id>/", unmark_to_meet, name="unmark-to-meet"),
    path("close-todo/<id>/", close_todo, name="close-todo"),
    path("close-to-meet/<id>/", close_to_meet, name="close-to-meet"),
    path("close-habit/<id>/", close_habit, name="close-habit"),
    path("mark-bookmark/<id>/", mark_habit, name="mark-bookmark"),
    path("unmark-bookmark/<id>/", unmark_habit, name="unmark-bookmark"),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

