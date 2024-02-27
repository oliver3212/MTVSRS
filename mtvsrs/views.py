from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction


# @login_required()
def home(request):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM User")
    row = cursor.fetchone()

    cursor.close()

    context = {
        'row': row,
    }
    return render(request, "home.html", context)

