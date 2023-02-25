from django.db import models

class Courses(models.Model):
    category = models.CharField(max_length=30)
    course_name = models.CharField(max_length=250)
    instructor = models.CharField(max_length=100)
    course_description = models.TextField()
    enrolled = models.IntegerField()
    ratings = models.IntegerField()

