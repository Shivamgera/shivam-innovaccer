import pickle
import pandas as pd
from .models import Movies, Genres

def get_movies_data():
    data = pd.read_csv("omdb_api/omdb/data_dir/data.csv", sep='\t')
    ratings = pd.read_csv("omdb_api/omdb/data_dir/ratings.tsv", sep="\t")
    out = (data.merge(ratings, left_on='tconst', right_on='tconst')
              .reindex(columns=['tconst', 'originalTitle', 'startYear', 'genres', 'averageRating']))
    return out


def get_genre_list():
    li = []
    data = pd.read_csv("data.csv", sep='\t')
    for item in data["genres"]:
	    item = str(item)
	    temp = item.split(",")
	    for i in temp:
		    if i not in li:
			    li.append(i)
    return li


def create_movies_in_database():
    movies = get_movies_data()
    for item in movies.index:
        Movies.create_movie(tconst=movies['tconst'][item], title=movies['originalTitle'][item], 
                year=movies['startYear'][item], rating=movies['averageRating'][item], genre=movies['genres'][item])
        


def create_genres_in_database():
    movies = get_movies_data()
    for item in movies.index:
        for genre in movies['genres'][item].split(','):
            Genres.create_genre(tconst=movies['tconst'][item], genre=genre)