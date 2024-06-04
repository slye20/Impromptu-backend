from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ..models import Post
from ..serializers.post_serializer import PostSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

class ImpromptuDetail(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404("Post not found.")

    # Get specific post
    def get(self, request, pk):
        post = self.get_post(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # update a post
    def put(self, request, pk):
        post = self.get_post(pk)
        if post.user != request.user:
            return Response({"message": "You do not have permission to update this post."}, status=status.HTTP_403_FORBIDDEN)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete a post
    def delete(self, request, pk):
        post = self.get_post(pk)
        if post.user != request.user:
            return Response({"message": "You do not have permission to update this post."}, status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
