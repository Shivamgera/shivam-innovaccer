from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.pagination import CursorPagination, LimitOffsetPagination
from django.db.models import Q
from rest_framework import filters
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Movies, Genres
from .serializers import MoviesSerializer



class CursorSetPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class MovieView(ListAPIView):
    serializer_class = MoviesSerializer
    pagination_class = CursorSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering = ['-rating']
    page_size_query_param = 'page_size'

    def get_queryset(self):
        movies = Movies.objects.all()
        genre_param = self.request.query_params.get('g', None)
        year = self.request.query_params.get('y', None)
        page_size = int(self.request.GET.get('page_size', 10))
        offset = self.request.GET.get('offset', 1)
        movies = movies.exclude(rating=None)
        if year:
            movies = movies.filter(Q(year=year))
            # movies = query_of_field(year, 'year')
        if genre_param:
            # movies = movies.filter(Q(genre__icontains=genre_param))
            queries = query_of_field(genre_param)
            movies = movies.filter(queries)
        return movies.values()


def query_of_field(query):
    if not query:
        return Q()
    query = query.replace('+', ' ').split(' ')
    temp_query = Q()
    for i in query:
        temp_query &= Q(genre__icontains=i)

    return temp_query


def redirect(request):
    return HttpResponseRedirect(reverse('omdb:movies'))