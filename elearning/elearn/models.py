from django.db import models
from django.contrib.auth.models import User


class Learner(User):
    # Add custom fields specific to learners here
    # (e.g., bio, profile picture URL)
    pass


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    students = models.ManyToManyField(Learner, blank=True)
    # Add other relevant fields (e.g., category, instructor, duration)


class Content(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Link content to a course
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50)  # Specify content type (e.g., video, text)
    content_url = models.URLField(blank=True)  # Optional URL for video content
    content_text = models.TextField(blank=True)  # Optional text content



class Progress(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)  # Link progress to a learner
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Link progress to a course
    completed_content = models.ManyToManyField(Content, blank=True)  # Track completed content
