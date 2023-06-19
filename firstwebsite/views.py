from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    welcome = "Welcome"
    choice = "Please choose something"
    return render(request, "./index.html", {
        'welcome':welcome,
        'choice':choice
    })
    # return HttpResponse("Hello Word точнее миша чепух")
