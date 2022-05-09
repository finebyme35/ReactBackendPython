from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CategorySerializer
from .models import Category
from rest_framework.response import Response
from django.utils import timezone

class CategoryListView(ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_active__in=[True])
    def perform_create(self, serializer):
        serializer.save()
        return serializer.data
    def put(self, request, pk):
        queryset = Category.objects.get(id=pk)
        serializer = CategorySerializer(queryset, many=False, data=request.data)
        if serializer.is_valid():
            queryset.updated_date = timezone.now()
            queryset.save()
            return Response({'status': 'category updated'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    def delete(self, request, pk):
        queryset = Category.objects.get(id=pk)
        serializer = CategorySerializer(queryset, many=False)
        if queryset is not None:
            queryset.is_active = False
            queryset.updated_date = timezone.now()
            queryset.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    