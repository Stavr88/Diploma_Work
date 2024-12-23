from rest_framework.serializers import ModelSerializer

from ads.models import Ads, Feedback


class AdsSerializer(ModelSerializer):
    """
    Сериализатор для модели Ads
    """

    class Meta:
        model = Ads
        fields = "__all__"


class FeedbackSerializer(ModelSerializer):
    """
    Сериализатор для модели Feedback
    """

    class Meta:
        model = Feedback
        fields = "__all__"


class FeedbackDetailSerializer(ModelSerializer):
    """
    Сериализатор для одного объекта Feedback
    """

    ads = AdsSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = "__all__"


class AdsDetailSerializer(ModelSerializer):
    """
    Сериализатор для одного объекта Ads
    """

    feedback = FeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = Ads
        fields = "__all__"
