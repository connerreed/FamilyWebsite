import os
from rest_framework import serializers
from .models import (FamilyMember, Recipe, RecipeContentImage, MealType, Picture, Video, Comment,
                     RecipeAlbum, MediaAlbum)

class RecipeContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeContentImage
        fields = ['id', 'image']

class RecipeSerializer(serializers.ModelSerializer):
    images = RecipeContentImageSerializer(many=True, write_only=True)
    mealType = serializers.SlugRelatedField(slug_field='name', queryset=MealType.objects.all(), many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'user', 'recipeAuthor', 'mealType', 'featured', 'thumbnail', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        recipe = Recipe.objects.create(**validated_data)
        for image_data in images_data:
            RecipeContentImage.objects.create(recipe=recipe, **image_data)
        return recipe
    
    def update(self, instance, validated_data):
        images_data = validated_data.pop('images')
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.user = validated_data.get('user', instance.user)
        instance.recipeAuthor = validated_data.get('recipeAuthor', instance.recipeAuthor)
        instance.mealType.set(validated_data.get('mealType', instance.mealType))
        instance.featured = validated_data.get('featured', instance.featured)
        instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)
        instance.save()

        # Clear existing images and add new ones
        instance.images.all().delete()
        for image_data in images_data:
            RecipeContentImage.objects.create(recipe=instance, **image_data)

        return instance
    
class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def validate_video(self, value):
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm']
        if not ext.lower() in valid_extensions:
            raise serializers.ValidationError('Unsupported file type. Please upload a video file.')
        return value
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class RecipeAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeAlbum
        fields = '__all__'

class MediaAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAlbum
        fields = '__all__'

class FamilyMemberNestedSerializer(serializers.ModelSerializer):
    picture_url = serializers.SerializerMethodField()
    class Meta:
        model = FamilyMember
        fields = ['id', 'name', 'birthday', 'deathday', 'bio', 'picture_url']

    def get_picture_url(self, obj):
        request = self.context.get('request')
        if request and hasattr(obj.picture, 'url'):
            return request.build_absolute_uri(obj.picture.url)
        return None


class FamilyMemberSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    spouse_detail = serializers.SerializerMethodField()
    parents = serializers.SerializerMethodField()
    picture_url = serializers.SerializerMethodField()

    class Meta:
        model = FamilyMember
        fields = ['id', 'name', 'birthday', 'deathday', 'bio', 'picture_url', 'father', 'mother', 'spouse', 'children', 'spouse_detail', 'parents']

    def get_children(self, instance):
        children = instance.children.all()
        return FamilyMemberNestedSerializer(children, many=True, context=self.context).data

    def get_spouse_detail(self, instance):
        if instance.spouse:
            return FamilyMemberNestedSerializer(instance.spouse, context=self.context).data
        return None

    def get_parents(self, instance):
        parents = [instance.father, instance.mother]
        return FamilyMemberNestedSerializer([parent for parent in parents if parent], many=True, context=self.context).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Add string representation of related objects
        representation['father'] = instance.father.name if instance.father else None
        representation['mother'] = instance.mother.name if instance.mother else None
        representation['spouse'] = instance.spouse.name if instance.spouse else None
        return representation

    def get_picture_url(self, obj):
        request = self.context.get('request')
        if request and hasattr(obj.picture, 'url'):
            return request.build_absolute_uri(obj.picture.url)
        return None

