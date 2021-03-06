from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    """
    分类
    """

    name = models.CharField('名称', max_length=16)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签
    """

    name = models.CharField('名称', max_length=16)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    博客
    """

    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('正文')
    created_time= models.DateTimeField('发布时间', auto_now_add=True)
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_time']
