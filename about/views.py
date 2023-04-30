from django.shortcuts import render

# Create your views here.


def ORGANISATION_OF_MINISTRY_OF_DEFENCE(request):
    template_name="about/ORGANISATION_OF_MINISTRY_OF_DEFENCE.html"
    title = "About Us"
    last = "Organisation of Ministry of Defence"
    context={
        "title" : title,
        "last" : last
    }
    return render(request, template_name, context)


def STRUCTURE_OF_ARMY(request):
    template_name="about/STRUCTURE_OF_ARMY.html"
    title = "About Us"
    last = "STRUCTURE OF ARMY"
    context={
        "title" : title,
        "last" : last
    }
    return render(request, template_name, context)



def Our_Ethos(request):
    template_name="about/Our_Ethos.html"
    title = "About Us"
    last = "Our Ethos"
    context={
        "title" : title,
        "last" : last
    }
    return render(request, template_name, context)



def THEME_OF_THE_YEAR(request):
    template_name="about/THEME_OF_THE_YEAR.html"
    
    title = "About Us"
    last = "THEME OF THE YEAR 2023"
    context={
        "title" : title,
        "last" : last
    }
    return render(request, template_name, context)
