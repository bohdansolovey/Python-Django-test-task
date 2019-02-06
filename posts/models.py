from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils import timezone

from restFull import settings
from users.models import CustomUser


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                .filter(status='published')

class Post(models.Model ):
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
            )
    title = models.CharField(u'Заголовок',max_length=80)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(CustomUser, related_name='posts',default="1", on_delete=models.CASCADE)

    author.verbose_name='Автор'
    body = models.TextField(u'Опис')
    publish = models.DateTimeField(u'Опубліковано',default=timezone.now)
    created = models.DateTimeField(u'Створено',auto_now_add=True)
    updated = models.DateTimeField(u'Оновлено',auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    objects = models.Manager()
    published = PublishedManager()
    img = models.ImageField(upload_to='images/', default='images/no_ing.jpg', blank=True,null=True)


    class Meta:
        ordering = ('-publish', )
        verbose_name = u"Оголошення"
        verbose_name_plural = u'Оголошення'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
            self.publish.strftime('%m'),
            self.publish.strftime('%d'),
            self.slug])


