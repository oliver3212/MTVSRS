from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction


# @login_required()
def home(request):
    context = {
        'card_count': range(10)
    }
    return render(request, "home.html", context)

