from django.shortcuts import render
from mtvsrs.models import Movie
from django.contrib.auth.decorators import login_required


# @login_required()
def home(request):

    # change to shows, and change variable name to be new_release_shows
    movies = Movie.objects.filter(release_date__isnull=False).order_by('-release_date')[:10]

    context = {
        'card_count': range(10),
        'movies': movies
    }
    return render(request, "home.html", context)

