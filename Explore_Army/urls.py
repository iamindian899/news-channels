from django.urls import path

from . import views

urlpatterns = [
    path("", views.Explore_Army, name="Explore_Army"),
    path("adventure-activities/", views.Adventure_Activities, name="Adventure_Activities"),
    path("war-memorials/", views.War_Memorials, name="War_Memorials"),
]