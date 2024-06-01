from rest_framework import serializers
from .models import FamilyMember, Recipe, RecipeContentImage, MealType

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

class FamilyMemberNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = ['id', 'name', 'birthday', 'deathday', 'bio', 'picture']

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
        return FamilyMemberNestedSerializer(children, many=True).data

    def get_spouse_detail(self, instance):
        if instance.spouse:
            return FamilyMemberNestedSerializer(instance.spouse).data
        return None

    def get_parents(self, instance):
        parents = [instance.father, instance.mother]
        return FamilyMemberNestedSerializer([parent for parent in parents if parent], many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Add string representation of related objects
        representation['father'] = instance.father.name if instance.father else None
        representation['mother'] = instance.mother.name if instance.mother else None
        representation['spouse'] = instance.spouse.name if instance.spouse else None
        return representation
    
    def get_picture_url(self, obj):
        request = self.context.get('request')
        if obj.picture:
            return request.build_absolute_uri(obj.picture.url)
        return None

