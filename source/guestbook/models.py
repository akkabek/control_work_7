from django.db import models

STATUS_CHOICES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано'),
]
class GuestbookEntry(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name='Автор')
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name='Почта')
    content = models.TextField(null=False, blank=False, verbose_name='Текст записи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name='Статус'
    )
    class Meta:
        db_table = 'guestbook_entry'
        verbose_name = 'Запись в гостевую книгу'
        verbose_name_plural = 'Записи в гостевую книгу'

    def __str__(self):
        return f'{self.pk}. {self.author}'