from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="Training_Establishment"),
    path("inter-services-establishments/", views.Inter_Services_Establishments, name="Inter_Services_Establishments"),
    path("army-establishments/", views.Army_Establishments, name="Army_Establishments"),
    path("training-team/", views.Training_Team, name="Training_Team"),
    path("rashtriya-military-schools/", views.Rashtriya_Military_Schools, name="Rashtriya_Military_Schools"),
    path("ignou-army-education-project-iaep/", views.Army_Education_Project, name="Army_Education_Project"),
    
]