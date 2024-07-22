from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    type = models.CharField(null = False)
    title = models.CharField(max_length = 100, null = False)
    description = models.TextField(null=True)
    location = models.CharField(max_length = 180, null = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = False)
    name = models.CharField(max_length = 100, blank=False, null = False)
    email = models.EmailField(null = False, blank=False)
    phone = models.CharField(max_length = 20, blank=True, null = True)
    additional_info = models.TextField(null = True, blank=True)
    date = models.DateTimeField(blank = False, null = False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    longitude = models.FloatField(null = False)
    latitude = models.FloatField(null = False)
    report_count = models.IntegerField(default = 0)

    def __str__(self):
        return self.title
