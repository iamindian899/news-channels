from django.urls import path


from . import views

urlpatterns = [
    path("ORGANISATION OF MINISTRY OF DEFENCE/", views.ORGANISATION_OF_MINISTRY_OF_DEFENCE , name="ORGANISATION_OF_MINISTRY_OF_DEFENCE"),
    path("STRUCTURE OF ARMY/", views.STRUCTURE_OF_ARMY , name="STRUCTURE_OF_ARMY"),
    path("Our Ethos/", views.Our_Ethos , name="Our_Ethos"),
    path("THEME OF THE YEAR/", views.THEME_OF_THE_YEAR , name="THEME_OF_THE_YEAR"),
]