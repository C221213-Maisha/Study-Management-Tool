# models.py
from django.db import models
from django.conf import settings  # Import settings

class ClassSchedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL instead of 'auth.User'
    day = models.CharField(max_length=100)
    slot = models.CharField(max_length=100)
    course_name = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=200)
    class_time = models.CharField(max_length=100)
    classroom_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course_name} on {self.day} at {self.class_time}"
