from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Post
from .serializers import ImpromptuSerializer

class ImpromptuList(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    # List all posts
    def get(self, request):
        posts = Post.objects.all()
        serializer = ImpromptuSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = {
            'title': request.data.get("title"),
            'description': request.data.get("description"),
            'location': request.data.get("location")
        }

        serializer = ImpromptuSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
