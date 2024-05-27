from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class MealType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='recipes')
    recipeAuthor = models.CharField(max_length=100)
    mealType = models.ManyToManyField(MealType, related_name='recipes')
    featured = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='images/recipethumbnails/')

    def __str__(self):
        return f'{self.title} - {self.recipeAuthor}'


class RecipeContentImage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/recipecontent/')


class Picture(models.Model):
    image = models.ImageField(upload_to='images/pictures/')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='pictures')


class Video(models.Model):
    video = models.FileField(upload_to='videos/')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='videos')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.user.username} - {self.content[:20]}'


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.user.username} - {self.score}'


class RecipeAlbum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_albums')
    recipes = models.ManyToManyField(Recipe, related_name='albums')

    def __str__(self):
        return self.title


class MediaAlbum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media_albums')
    pictures = models.ManyToManyField(Picture, related_name='media_albums', blank=True)
    videos = models.ManyToManyField(Video, related_name='media_albums', blank=True)

    def __str__(self):
        return self.title

# Family Tree
class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    bio = models.TextField()
    father = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='children', null=True, blank=True)
    mother = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='children2', null=True, blank=True)
    spouse = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='spouses', null=True, blank=True)
    picture = models.ImageField(upload_to='images/familytree/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    

class FamilyTree(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    root = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='family_tree')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='family_trees')

    def __str__(self):
        return self.title