from django.urls import path
from Category import views
app_name = 'category'

urlpatterns = [
    path('', views.CategoryListView.as_view(), name="list"),
    path('<int:pk>', views.CategoryDetailView.as_view(), name="detail"),
    path('creates/', views.CategoryListView.as_view(), name="create"),
]