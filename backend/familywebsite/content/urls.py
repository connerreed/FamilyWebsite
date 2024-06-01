from django.urls import path
from . import views

urlpatterns = [
    path('familymembers/', views.FamilyMemberListCreateView.as_view(), name='familymember-list-create'),
    path('familymembers/<int:pk>/', views.FamilyMemberRetrieveUpdateDestroyView.as_view(), name='familymember-retrieve-update-destroy')
]