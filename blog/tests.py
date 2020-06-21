import datetime

from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from mock import Mock

from blog.models import Post
from blog.serializers import PostSerializer

# Errors found. Not working good.
class TestPostSerializer:

    def test_expected_serialized_json(self):
        post = Mock(spec=Post)

        expected_results = {
            'id': 1,
            'title': 'Post 1',
            'slug': 'post-1',
            'author': 1,
            'content': 'Lorem ipsum',
            'updated_on': str(datetime.datetime.now()),
            'created_on': str(datetime.datetime.now()),
            'status': 0,
        }

        post = Post(**expected_results)

        results = PostSerializer(post).data

        assert results == expected_results

