from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, permissions
from posts.models import Post
from posts.serializers import PostSerializer
from users.models import CustomUser
from users.serializers import UserSerializer


class UserList(generics.ListAPIView):
    """
        List of all users
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
         detail information about  selected user
     """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer




class PostByAuthor(generics.ListAPIView):
    """
        allows you to view all the posts of the user who asks
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Post.objects.filter(author=user)

