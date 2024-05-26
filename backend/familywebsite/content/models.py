from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='recipes')
    recipeAuthor = models.CharField(max_length=100)
    mealType = models.CharField(max_length=100) # breakfast, lunch, dinner, snack, other


    def __str__(self):
        return f'{self.title} - {self.recipeAuthor}'


class Picture(models.Model):
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='pictures')


class Video(models.Model):
    video = models.FileField(upload_to='videos/')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='videos')

class Comment(models.Model):
    pass

class Rating(models.Model): # 1-5, on any content
    pass

class RecipeAlbum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_albums')
    recipes = models.ManyToManyField(Recipe, related_name='albums')

    def __str__(self):
        return self.title

class MediaAlbum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media_albums')
    pictures = models.ManyToManyField(Picture, related_name='media_albums', blank=True)
    videos = models.ManyToManyField(Video, related_name='media_albums', blank=True)

    def __str__(self):
        return self.title