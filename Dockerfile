FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN python manage.py collectstatic --noinput

CMD gunicorn omdb_api.wsgi:application --bind 0.0.0.0:$PORT