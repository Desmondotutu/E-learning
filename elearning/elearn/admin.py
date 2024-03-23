from django.contrib import admin
from .models import Course, Content, Progress  # Import your models

# Register your models with the admin interface
admin.site.register(Course)
admin.site.register(Content)
admin.site.register(Progress)
