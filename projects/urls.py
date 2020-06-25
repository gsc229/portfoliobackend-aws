from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from projects import views

urlpatterns = [
    path('', views.api_root),
    path('projects/', views.ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>', views.ProjectDetail.as_view(), name='project-detail')
]
