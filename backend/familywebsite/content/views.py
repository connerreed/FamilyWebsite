from rest_framework import generics
from django.shortcuts import render
from .models import (FamilyMember, Recipe, Picture, Video, Comment, RecipeAlbum, MediaAlbum)
from .serializers import (FamilyMemberSerializer, RecipeSerializer, PictureSerializer, VideoSerializer,
                          CommentSerializer, RecipeAlbumSerializer, MediaAlbumSerializer)

# Create your views here.
class FamilyMemberListCreateView(generics.ListCreateAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer

class FamilyMemberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class PictureListCreateView(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class PictureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RecipeAlbumListCreateView(generics.ListCreateAPIView):
    queryset = RecipeAlbum.objects.all()
    serializer_class = RecipeAlbumSerializer

class RecipeAlbumRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeAlbum.objects.all()
    serializer_class = RecipeAlbumSerializer

class MediaAlbumListCreateView(generics.ListCreateAPIView):
    queryset = MediaAlbum.objects.all()
    serializer_class = MediaAlbumSerializer

class MediaAlbumRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MediaAlbum.objects.all()
    serializer_class = MediaAlbumSerializer