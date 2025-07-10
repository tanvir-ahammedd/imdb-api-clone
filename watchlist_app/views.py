from django.shortcuts import render
from . models import Movie
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)

def movie_data(request, pk):
    movie = Movie.objects.get(pk=pk)
    # manual dictionary
    # data = {
    #     'name': movie.name,
    #     'description': movie.description,
    #     'activ': movie.active
    # }
    data = {
        'movie': model_to_dict(movie)
    }
    return JsonResponse(data)
    