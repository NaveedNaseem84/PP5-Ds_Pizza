from django.shortcuts import render


def aboutus_view(request):

    return render(request, 'about/about.html')
