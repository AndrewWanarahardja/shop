from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406407373',
        'name': 'Andrew Wanarahardja',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)