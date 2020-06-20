import datetime

from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from mock import Mock

from blog.models import Post
from blog.serializers import PostSerializer


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

    # def test_raise_error_when_missing_required_field(self):
    #     incomplete_data = {
    #         'name': 'Ferrari',
    #         'code': 'fr1',
    #         'created': str(datetime.datetime.now()),
    #         'modified': str(datetime.datetime.now())
    #     }
    #
    #     serializer = CarSerializer(data=incomplete_data)
    #
    #     # Este ContextManager nos permite verificar que
    #     # se ejecute correctamente una Excepcion
    #     with pytest.raises(ValidationError):
    #         serializer.is_valid(raise_exception=True)