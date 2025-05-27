from django.shortcuts import render

# Create your views here.


def management_view(request):

    return render(request, 'management/management.html')
    