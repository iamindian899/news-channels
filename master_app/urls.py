from django.urls import path


from . import views

urlpatterns = [
    
    path("" , views.home, name="master_home"),
    path("publications" , views.Publications, name="Publications"),
    path("un-journal" , views.UN_Journal, name="UN_Journal"),
    path("artrac-pinnacle-journal-2022" , views.ARTRAC_Pinnacle_Journal_2022, name="ARTRAC_Pinnacle_Journal_2022"),
    path("publications/baatcheet" , views.publications, name="publications"),
    path("knowledge-online" , views.Knowledge_Online, name="Knowledge_Online"),
    path("friends-for-life" , views.Friends_For_Life, name="Friends_For_Life"),
    path("media-release" , views.Media_Release, name="Media_Release"),
    path("photo-gallery" , views.Photo_Gallery, name="Photo_Gallery"),
    path("gallery" , views.gallery, name="gallery"),
    path("army-design-bureau" , views.Army_Design_Bureau, name="Army_Design_Bureau"),
    path("tender-and-rfi" , views.Tender_and_RFI, name="Tender_and_RFI"),
    path("RFIs" , views.RFIs, name="RFIs"),
    path("Archive" , views.Archive, name="Archive"),
    path("contact-us" , views.Contact_us, name="Contact_us"),
    path("external-links" , views.External_Links, name="External_Links"),
    path("FAQ" , views.FAQ, name="FAQ"),
    path("right-to-information" , views.Right_to_Information, name="Right_to_Information"),
    path("privacy-policy" , views.Privacy_Policy, name="Privacy_Policy"),

]


