from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Commandant/", views.Commandant, name="Commandant"),
    path("Previous Commandants/", views.Previous_Commandants, name="Previous_Commandants"),
    path("Insignia and Moto/", views.Insignia_and_Moto, name="Insignia_and_Moto"),
    path("Role and Tasks/", views.The_Infantry_SchoolRole_and_Tasks, name="The_Infantry_SchoolRole_and_Tasks"),
    path("Raising School/", views.Raising_School, name="Raising_School"),
    path("Army Rifle Association/", views.Army_Rifle_Association, name="Army_Rifle_Association"),
    path("Infantry Journal/", views.Infantry_Journal, name="Infantry_Journal"),
    path("About Mhow/", views.About_Mhow, name="About_Mhow"),
    path("History of Mhow/", views.History_of_Mhow, name="History_of_Mhow"),
    path("Geography/", views.Geography, name="Geography"),
    path("Directions and Maps/", views.Directions_and_Maps, name="Directions_and_Maps"),
    # path("Training Establishments/", views.Training_Establishments, name="Training_Establishments"),
    # path("Explore Army/", views.Explore_Army, name="Explore_Army"),
    

]