from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Task(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        unique=True
    )
    description = models.TextField(
        max_length=300,
        verbose_name='Описание',
        blank=True, null=True
    )
    is_completed = models.BooleanField(
        verbose_name='Статус',
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    image = models.ImageField(
        upload_to='todo_images/',
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"