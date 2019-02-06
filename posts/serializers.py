from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    img = serializers.ImageField(use_url=True, allow_null=True, max_length= None)
    class Meta:
        model = Post
        fields = ('id','title', 'body','author','img')
