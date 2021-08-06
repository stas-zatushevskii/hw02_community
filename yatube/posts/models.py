from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='группы')
    slug = models.SlugField(unique=True, verbose_name='слуг')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        default_related_name = 'posts'
        verbose_title = 'название группы'


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(Group, blank=True,
                              null=True, on_delete=models.CASCADE,
                              related_name='posts')
