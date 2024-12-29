from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny

from ads.models import Ads, Feedback
from ads.paginators import CustomPagination
from ads.serializers import (AdsDetailSerializer, AdsSerializer, FeedbackDetailSerializer, FeedbackSerializer)
from ads.services import get_user_permissions


class AdsCreateAPIView(CreateAPIView):
    """
    Класс для создания объекта модели Ads
    """

    serializer_class = AdsSerializer

    def perform_create(self, serializer):
        """
        Переопределение метода для автоматической привязки владельца к создаваемому объекту
        """
        serializer.save(author=self.request.user)


class AdsListAPIView(ListAPIView):
    """
    Класс для просмотра списка объектов модели Ads
    """

    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ("title", "author",)
    pagination_class = CustomPagination


class AdsRetrieveAPIView(RetrieveAPIView):
    """
    Класс для просмотра одного объекта модели Ads
    """

    queryset = Ads.objects.all()
    serializer_class = AdsDetailSerializer


class AdsUpdateAPIView(UpdateAPIView):
    """
    Класс для обновления объекта модели Ads
    """

    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

    # def get_permissions(self):
    #     """
    #     Возвращает права доступа в зависимости от прав пользователя
    #     """
    #     return [permission() for permission in get_user_permissions(self.request)]

    def get_permissions(self):
        """
        Возвращает права доступа в зависимости от прав пользователя
        """
        return get_user_permissions(self.request)


class AdsDestroyAPIView(DestroyAPIView):
    """
    Класс для удаления объекта модели Ads
    """

    queryset = Ads.objects.all()

    def get_permissions(self):
        """
        Возвращает права доступа в зависимости от прав пользователя
        """
        return get_user_permissions(self.request)


class FeedbackCreateAPIView(CreateAPIView):
    """
    Класс для создания объекта модели Feedback
    """

    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        """
        Переопределение метода для автоматической привязки владельца к создаваемому объекту
        """
        serializer.save(author=self.request.user)


class FeedbackListAPIView(ListAPIView):
    """
    Класс для просмотра списка объектов модели Feedback
    """

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackRetrieveAPIView(RetrieveAPIView):
    """
    Класс для просмотра одного объекта модели Feedback
    """

    queryset = Feedback.objects.all()
    serializer_class = FeedbackDetailSerializer


class FeedbackUpdateAPIView(UpdateAPIView):
    """
    Класс для обновления объекта модели Feedback
    """

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_permissions(self):
        """
        Возвращает права доступа в зависимости от прав пользователя
        """
        return get_user_permissions(self.request)


class FeedbackDestroyAPIView(DestroyAPIView):
    """
    Класс для удаления объекта модели Feedback
    """

    queryset = Feedback.objects.all()

    def get_permissions(self):
        """
        Возвращает права доступа в зависимости от прав пользователя
        """
        return get_user_permissions(self.request)
