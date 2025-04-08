from django.conf import settings
from django.db import models


class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"


class Advertisement(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

class UserThrottle(UserRateThrottle):
    rate = '20/min'


class AnonThrottle(AnonRateThrottle):
    rate = '10/min'


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()

    def perform_update(self, serializer):
        advertisement = self.get_object()

        if advertisement.status == AdvertisementStatusChoices.CLOSED and serializer.validated_data.get(
                'status') == AdvertisementStatusChoices.OPEN:

            pass

        if advertisement.creator != self.request.user:
            raise PermissionDenied("У вас нет прав для изменения этого объявления.")

        serializer.save()

    def perform_destroy(self, instance):
        if instance.creator != self.request.user:
            raise PermissionDenied("У вас нет прав для удаления этого объявления.")

        instance.delete()