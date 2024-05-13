from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Note
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
  serializer_class = NoteSerializer
  permission_classes = [IsAuthenticated]


class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]
