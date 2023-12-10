from rest_framework import generics
from .models import ForumCategory
from .serializer import ForumCategorySerialzier

# Create your views here.
class ForumCategoryListView(generics.ListCreateAPIView):
  queryset = ForumCategory.objects.all()
  serializer_class = ForumCategorySerialzier