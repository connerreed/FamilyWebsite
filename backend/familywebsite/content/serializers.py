from rest_framework import serializers
from .models import FamilyMember

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

