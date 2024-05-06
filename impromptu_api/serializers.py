from rest_framework import serializers
from .models import Post

class ImpromptuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "description", "location", "timestamp", "updated", "user"]