# posts/views.py
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request, format=None):
    """
    :param request:
    :param format:
    :return: list of available buttons
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format),
        'docs': reverse('docs', request=request, format=format)
    })

class PostList(generics.ListCreateAPIView):
    """
        returns list of all posts and give opportunity to create new posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        """
            method that give ability to add new post

        """
        serializer.save(author=self.request.user)



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Detail information about selected post with ability to add new post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


