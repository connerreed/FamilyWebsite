from django.urls import path
from . import views

urlpatterns = [
    path('familymembers/', views.FamilyMemberListCreateView.as_view(), name='familymember-list-create'),
    path('familymembers/<int:pk>/', views.FamilyMemberRetrieveUpdateDestroyView.as_view(), name='familymember-retrieve-update-destroy'),
    path('recipes/', views.RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', views.RecipeRetrieveUpdateDestroyView.as_view(), name='recipe-retrieve-update-destroy'),
]