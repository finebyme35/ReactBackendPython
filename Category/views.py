from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from .serializers import CategorySerializer
from .models import Category
from rest_framework.response import Response
from django.utils import timezone

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active__in=[True])
    permission_classes = (AllowAny, )
    def post(self, request, pk=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



    def destroy(self, request, pk):
        queryset = Category.objects.get(id=pk)
        serializer = Category(queryset, many=False)
        if queryset is not None:
            queryset.is_active = False
            queryset.updated_date = timezone.now()
            queryset.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        queryset = Category.objects.get(id=pk)
        serializer = CategorySerializer(queryset, many=False, data=request.data)
        if serializer.is_valid():
            queryset.updated_date = timezone.now()
            queryset.save()
            return Response({'status': 'category updated'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

