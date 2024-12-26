from rest_framework.pagination import PageNumberPagination

from config import settings

from django.utils.translation import gettext_lazy as _


class CustomPagination(PageNumberPagination):
    """
    Кастомная реализация пагинации
    """
    page_size = settings.PAGE_SIZE
    page_size_query_param = "page_size"
    max_page_size = settings.MAX_PAGE_SIZE
    page_size_query_description = _('Количество результатов, возвращаемых на страницу')

