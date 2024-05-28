from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User
from ..serializers.user_serializer import UserSerializer

class ImpromptuUser(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    # Create user
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
