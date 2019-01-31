from rest_framework import serializers
from posts.models import Post
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post.objects.all())

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'posts','email')