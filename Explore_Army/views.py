from django.shortcuts import render

# Create your views here.


def Explore_Army(request):
    template_name="Explore_Army/index.html"
    context={
    
    }
    return render(request, template_name, context)


def Adventure_Activities(request):
    template_name="Explore_Army/Adventure_Activities.html"
    context={
    
    }
    return render(request, template_name, context)


def War_Memorials(request):
    template_name="Explore_Army/War_Memorials.html"
    context={
    
    }
    return render(request, template_name, context)
