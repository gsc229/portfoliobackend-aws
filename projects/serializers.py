from rest_framework import serializers
from rest_framework.fields import MultipleChoiceField
from projects.models import Project
from django.contrib.auth.models import User
from projects.tech_choices import TECH_CHOICES, TYPE_CHOICES
from pygments.lexers import get_all_lexers, get_lexer_by_name

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
  technologies = serializers.MultipleChoiceField(choices=TECH_CHOICES)
  owner = serializers.ReadOnlyField(source='owner.username')
  class Meta:
    model = Project
    fields = [
                'id',
                'url',
                'title',                
                'owner',
                'project_type', 
                'top_photo', 
                'front_end_repo', 
                'back_end_repo',
                'website',
                'web_icon', 
                'description', 
                'roles', 
                'responsibilities',
                'technologies',
                'featured', 
                'created_at'
                ]

  def create(self, validated_data):
        return Project.objects.create(**validated_data)
        
  def update(self, instance, validated_data):
      instance.title = validated_data.get('title', instance.title)
      instance.project_type = validated_data.get('project_type', instance.project_type)
      instance.top_photo = validated_data.get('top_photo', instance.top_photo)
      instance.front_end_repo = validated_data.get('front_end_repo', instance.front_end_repo)
      instance.back_end_repo = validated_data.get('back_end_repo', instance.back_end_repo)
      instance.web_icon = validated_data.get('web_icon', instance.web_icon)
      instance.website = validated_data.get('website', instance.website)
      instance.description = validated_data.get('description', instance.description)
      instance.roles = validated_data.get('roles', instance.roles) 
      instance.responsibilities = validated_data.get('responsibilities', instance.responsibilities)        
      instance.technologies = validated_data.get('technologies', instance.technologies)
      instance.featured = validated_data.get('featured', instance.featured)
      instance.created_at = validated_data.get('created_at', instance.created_at)
      instance.save()
      return instance