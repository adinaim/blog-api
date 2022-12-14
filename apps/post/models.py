from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

from .utils import get_time


User = get_user_model()

class Post(models.Model):

    STATUS_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('draft', 'Draft')
    )
    
    user = models.ForeignKey(
        verbose_name='Автор поста',
        to=User,
        on_delete=models.CASCADE,
        related_name='publications'
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, primary_key=True, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='post_images')
    status = models.CharField(
        max_length=12, 
        choices=STATUS_CHOICES,
        default='draft')
    tag = models.ManyToManyField(
        to='Tag',
        related_name='publications',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + get_time())
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ('created_at', )


class Tag(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(primary_key=True, blank=True, max_length=35)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) # + str(self.created_at)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment from {self.user.username} to {self.post.title}'










# проверить в сандере запросы
# прочитать документации
# составить список тем для повторения, расписание
# посмореть больше видео с проектами на джанго
# читать книги, про компы, про интернет
# посмотреть все видео по джанго, сделать конспекты
# сравнить проекты, которые мы уже написали
# разобраться с celery и redis
# выписать все импорты по разным библиотекам и дать краткое описание
# прочитать про routers