from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ..models import Post
from ..serializers.post_serializer import PostSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

class ImpromptuList(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated] # Only authenticated uses

    # List all posts
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create a post
    def post(self, request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            try:
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
