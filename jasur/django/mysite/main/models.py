from django.db import models

# Create your models here.
class Author(models.Model):
    on_delete = None
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.last_name

class Book(models.Model):
    title = models.CharField(max_length=200, default='title')
    description = models.TextField()
    count = models.IntegerField()
    genre = models.CharField(max_length=100)
    pub_date = models.DateField()
    author_id = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Country(models.Model):
    name = models.CharField(max_length=200)
    desk = models.TextField()
    capital = models.CharField(max_length=100)
    square = models.IntegerField()
    logo = models. ImageField(upload_to='upload', blank=True, null= True, default='')

    def __str__(self):
        return self.name


class Chelsea(models.Model):
    club_name = models.CharField(max_length=100)
    best_player = models.CharField(max_length=100)
    golkiper = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)

    def __str__(self):
        return self.club_name
