from django.contrib import admin
from .models import Recipe, Picture, Video, Comment, Rating, RecipeAlbum, MediaAlbum
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Picture)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(RecipeAlbum)
admin.site.register(MediaAlbum)