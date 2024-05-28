from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ..models import Post
from ..serializers.post_serializer import PostSerializer

class ImpromptuDetail(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    # Get specific post
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # update a post
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete a post
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
