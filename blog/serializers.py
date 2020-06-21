from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    summary = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        read_only_fields = ('slug', 'author',)
        fields = '__all__'
