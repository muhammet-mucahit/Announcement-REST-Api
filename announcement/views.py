from django.shortcuts import render

def ApiHomepage(request):
    return render(request, 'api/Homepage.html', {})