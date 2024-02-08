from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}

STATUS_CHOICE = [
    ('Нуждаюсь в помощи', 'Нуждаюсь в помощи'),
    ('Готов помочь', 'Готов помочь'),
    ('Представитель благотворительной организации', 'Представитель благотворительной организации')
]


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона', **NULLABLE)
    photo = models.ImageField(verbose_name='Фото', upload_to='user/', **NULLABLE)
    town = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    status = models.CharField(max_length=150, verbose_name='Статус пользователя', default='Статус неопределён', choices=STATUS_CHOICE)
    is_active = models.BooleanField(default=True, verbose_name='Активирован')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('email', 'full_name', 'status')
