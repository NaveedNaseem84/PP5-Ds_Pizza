from django.shortcuts import render


def aboutus_view(request):
    """
    Renders the about us content.

    ***Template:***
        :template:`about/aboutus.html`
    """

    return render(request, 'about/about.html')
