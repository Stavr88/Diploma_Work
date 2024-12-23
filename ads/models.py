from django.db import models

from django.utils.translation import gettext_lazy as _, gettext

from config.settings import AUTH_USER_MODEL


def datepublished(date):
    """
    Функция для преобразования даты в удобочитаемый вид
    :param date: "DateTimeField"
    :return: "DateTimeField"
    """
    return _(date.strftime('%d.%m.%Y'))


class Ads(models.Model):
    """
    Модель объявления
    """

    title = models.CharField(
        max_length=100,
        verbose_name=_("Наименование товара"),
        help_text=_("Укажите наименование товара"),
        blank=True,
        null=True,
    )
    price = models.IntegerField(
        verbose_name=_("Цена на товар"),
        help_text=_("Укажите цену на товар"),
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name=_("Описание товара"),
        help_text=_("Опишите товар"),
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Дата создания записи"),
        help_text=_("Введите дату, по умолчанию установится текущая дата"),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _("Объявление")
        verbose_name_plural = _("Объявления")

    def __str__(self):
        """
        Строковое отображение объекта
        """
        return f'{self.title}-{self.price} руб., объявление добавлено - {datepublished(self.created_at)}г.'


class Feedback(models.Model):
    """
    Модель отзыва
    """
    text = models.TextField(
        verbose_name=_("Текст отзыва"),
        help_text=_("Оставьте свой отзыв"),
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        blank=True,
        null=True,
    )
    ad = models.ForeignKey(
        Ads,
        on_delete=models.CASCADE,
        verbose_name=_('Объявление'),
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Дата создания отзыва"),
        help_text=_("Введите дату, по умолчанию установится текущая дата"),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")

    def __str__(self):
        return f"{self.ad} ({self.author}, дата отзыва - {datepublished(self.created_at)}г.)"


