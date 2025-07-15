from django.urls import path
# from .views import movie_list, movie_details
from .views import MovieList, MovieDetails

urlpatterns = [
    path('list/', MovieList.as_view(), name="movie-list"),
    path('list/<int:pk>', MovieDetails.as_view(), name="movie-details"),
]