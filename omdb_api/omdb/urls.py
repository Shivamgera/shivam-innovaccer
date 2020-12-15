from django.urls import path, include
from .views import MovieView

urlpatterns = [
    path(r"movies/", MovieView.as_view(), name='movies'),
]