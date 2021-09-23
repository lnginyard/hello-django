from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse


# Create your views here.

def index(request):
    now = datetime.now()

    return render(
        request,
        "index_view.html",
        # Relative path from the 'templates'\
        # folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {



            'title': "Django!",
            'message': "Hello World...",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

