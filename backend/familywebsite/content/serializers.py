from rest_framework import serializers
from .models import Recipe, Picture, Video, Comment, Rating, RecipeAlbum, MediaAlbum

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video', 'user']

    def validate_video(self, value):
        extension = value.name.split('.')[-1].lower()
        valid_extensions = ['mp4', 'mov', 'avi', 'mkv', 'wmv']
        if extension not in valid_extensions:
            raise serializers.ValidationError('Invalid file. Please upload a video file.')
        return value