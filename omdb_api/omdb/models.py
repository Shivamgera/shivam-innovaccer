from django.db import models

# Create your models here.

class Movies(models.Model):
    created = models.DateTimeField(auto_now=True)
    tconst = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=512)
    year = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    genre = models.TextField(default='No Genre')

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.title} & {self.rating}'

    @staticmethod
    def create_movie(tconst, title, year, rating, genre):
        if not Movies.objects.filter(tconst=tconst).exists():
            movie = Movies()
            movie.tconst = tconst
            movie.title = title
            try:
                movie.year = year
                movie.rating = rating
            except Exception as e:
                movie.year = 1000
                movie.rating = 1.0
            movie.genre = genre
            movie.save()
            return movie

    @staticmethod
    def get_movies_list():
        return Movies.objects.all()



class Genres(models.Model):
    movie = models.ForeignKey('Movies', on_delete=models.CASCADE)
    genre = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.movie} {self.genre}'

    @staticmethod
    def create_genre(tconst, genre):
        movie = Movies.objects.get(tconst=tconst)
        genres = Genres()
        genres.movie = movie
        genres.genre = genre
        genres.save()