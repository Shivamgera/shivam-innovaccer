# Generated by Django 3.1.4 on 2020-12-13 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('tconst', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
                ('genre', models.TextField(default='No Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=60)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='omdb.movies')),
            ],
        ),
    ]