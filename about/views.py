from django.shortcuts import render

# Create your views here.


def aboutus_view(request):

    return render(request, 'about/about.html')
    
