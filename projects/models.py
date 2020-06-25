from django.db import models
from datetime import datetime
from rest_framework.fields import MultipleChoiceField
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import ArrayField
from projects.tech_choices import TECH_CHOICES, TYPE_CHOICES
from pygments.lexers import get_all_lexers, get_lexer_by_name

# Create your models here.
class Project(models.Model):
  owner = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)
  title = models.CharField(max_length=200, unique=True)
  project_type = models.CharField(choices=TYPE_CHOICES, max_length=100, default='None')
  top_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
  front_end_repo = models.CharField(max_length=500, blank=True)
  back_end_repo = models.CharField(max_length=500, blank=True)
  website = models.CharField(max_length=500, blank=True)
  web_icon = models.CharField(max_length=100, blank=True)
  description = models.TextField(blank=True)
  roles = models.TextField(blank=True)  
  responsibilities = models.TextField(blank=True)
  technologies = MultiSelectField(choices=TECH_CHOICES, default='None')
  featured = models.BooleanField(default=False)  
  created_at = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return f"title: {self.title} created: {self.created_at}"
