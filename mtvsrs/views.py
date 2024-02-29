from django.shortcuts import render, redirect
from mtvsrs.models import Movie
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect

def register_user(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            success_url = reverse("index")
            return HttpResponseRedirect(success_url)
    else:
        form = UserCreationForm()

    context = {"form": form}

    return render(request, "registration/registration_form.html", context)


# @login_required()
def home(request):

    # change to shows, and change variable name to be new_release_shows
    movies = Movie.objects.filter(release_date__isnull=False).order_by('-release_date')[:10]

    context = {
        'card_count': range(10),
        'movies': movies
    }
    return render(request, "home.html", context)

def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        posts = Movie.objects.filter(name__contains=search_query)
        return render(request, 'post_search.html', {'query':search_query, 'posts':posts})
    else:
        return render(request, 'post_search.html',{})



