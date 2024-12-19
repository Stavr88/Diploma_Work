from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Модель для создания и хранения данных о пользователе, данные хранятся в базе данных, в данном проекте используется
    БД PostgreSQL, настройки можно посмотреть в файле config.settings.py в переменной DATABASES
    """
    CHOICES_USER_ROLE = {
        "user": "user",
        "admin": "admin"
    }

    username = None
    email = models.EmailField(
        unique=True,
        verbose_name=_("Почта"),
        help_text=_("Укажите почту"),
    )
    phone = models.CharField(
        max_length=50,
        verbose_name=_("Телефон"),
        help_text=_("Укажите номер телефона"),
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="users/image",
        blank=True,
        null=True,
        verbose_name=_("Фотография пользователя"),
        help_text=_("Загрузите фотографию"),
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name=_("Имя пользователя"),
        help_text=_("Укажите Ваше имя"),
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_("Фамилия пользователя"),
        help_text=_("Укажите Вашу фамилию"),
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=50,
        verbose_name=_("Страна"),
        help_text=_("Укажите страну"),
        blank=True,
        null=True,
    )
    token = models.CharField(
        max_length=100,
        verbose_name="Тоken",
        null=True,
        blank=True
    )
    last_login = models.DateTimeField(
        default=datetime.now,
        verbose_name=_("Время последнего посещения"),
        null=True,
        blank=True
    )
    role = models.CharField(
        max_length=100,
        choices=CHOICES_USER_ROLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        """
        Возвращает строковое представление объекта
        """
        return self.email

