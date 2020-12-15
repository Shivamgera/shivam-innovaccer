
This project takes the IMDB (OMDB) movies data in csv format, pushed the data in local database using a script.
Upon running the server it navigates to `/api/movies/` endpoint and lists all the movies sorted by high to low ratings.
You can also filter the movies by Year and set of genres, by passing the param as `y=2019` and g='drama'.
Moreover, you can limit the results per page by passing `page_size` param.

Example request:

`http://0.0.0.0:8000/api/movies/?y=2019&g=short+drama&page_size=2`


It will give a beautified serialized and paginated response.

## To run this project locally:

- clone this repo
- create vitual environment: `python -m virtualenv env`
- activate the virtual environment: `source env/bin/activate`

- install the requirements: `pip install -r requirements.txt`

### Without Using Docker:

- create the postgres database
- run the server: `python manage.py runserver`

### With Docker

- Build: `docker-compose build`
- Run: `docker-compose up`

