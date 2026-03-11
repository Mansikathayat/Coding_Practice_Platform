from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Problem
from .serializers import ProblemListSerializer, ProblemDetailSerializer


class ProblemListAPIView(generics.ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['difficulty', 'category']
    search_fields = ['title', 'description']


class ProblemDetailAPIView(generics.RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemDetailSerializer
    permission_classes = [IsAuthenticated]