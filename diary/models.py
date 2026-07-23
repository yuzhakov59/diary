from django.db import models

from users.models import User


class DiaryPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='previews/', verbose_name='Превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='владелец')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'дневник'
        verbose_name_plural = 'дневники'
