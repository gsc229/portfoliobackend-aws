from rest_framework import generics, renderers, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from projects.models import Project
from django.contrib.auth.models import User
from projects.serializers import ProjectSerializer

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
  
  return Response({
    'projects': reverse('project-list', request=request, format=format)
    
  })

""" GET all, POST """
class ProjectList(generics.ListCreateAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

""" GET single, PUT, DELTE """
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  permission_classes  = [permissions.IsAuthenticatedOrReadOnly]