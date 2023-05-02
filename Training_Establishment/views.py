from django.shortcuts import render

# Create your views here.
def index(request):
    template_name="Training_Establishment/index.html"
    context={
    
    }
    return render(request, template_name, context)



def Inter_Services_Establishments(request):
    template_name="Training_Establishment/Inter_Services_Establishments.html"
    context={
    
    }
    return render(request, template_name, context)


def Army_Establishments(request):
    template_name="Training_Establishment/Army_Establishments.html"
    context={
    
    }
    return render(request, template_name, context)


def Training_Team(request):
    template_name="Training_Establishment/Training_Team.html"
    context={
    
    }
    return render(request, template_name, context)



def Rashtriya_Military_Schools(request):
    template_name="Training_Establishment/Rashtriya_Military_Schools.html"
    context={
    
    }
    return render(request, template_name, context)


def Army_Education_Project(request):
    template_name="Training_Establishment/Army_Education_Project.html"
    context={
    
    }
    return render(request, template_name, context)


