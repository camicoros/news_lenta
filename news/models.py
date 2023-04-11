from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Post(models.Model):
    """Модель новостного поста."""
    name = models.CharField('Название', max_length=72, unique=True)
    slug = models.SlugField(
        'Слаг для URL', max_length=72, unique=True, db_index=False)
    description = models.TextField(
        'Описание', max_length=150, blank=True)
    text = models.TextField('Текст поста')
    create_date = models.DateTimeField(
        'Дата создания', auto_now_add=True, db_index=True)
    update_date = models.DateTimeField(
        'Дата обновления', auto_now=True, db_index=True)
    pub_date = models.DateTimeField(
        'Дата публикации', default=now, db_index=True)
    is_published = models.BooleanField('Опубликован', default=False)

    class Meta:
        verbose_name = 'Новостной пост'
        verbose_name_plural = 'Новостные посты'
        ordering = ('-pub_date', 'name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'news:post-detail',
            kwargs={'slug': self.slug}
        )
