from rest_framework import generics
from .models import FamilyMember
from .serializers import FamilyMemberSerializer

# Create your views here.
class FamilyMemberListCreateView(generics.ListCreateAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer

class FamilyMemberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer