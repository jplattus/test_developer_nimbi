from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from blog.utils import unique_slugify, strip_tags


class Post(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('author'), related_name='blog_posts')
    content = models.TextField(_('content'), )
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    @property
    def summary(self):
        sum = strip_tags(self.content)
        sum = sum[:100] + '...'
        return sum

    def save(self, **kwargs):
        unique_slugify(self, self.title)
        super(Post, self).save(**kwargs)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
