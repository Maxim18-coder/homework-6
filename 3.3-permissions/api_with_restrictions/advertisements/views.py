from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAuthor()]
        return []

    def perform_destroy(self, instance):
        self.check_object_permissions(self.request, instance)
        instance.delete()

    def get_queryset(self):
        queryset = super().get_queryset()
        # Например, можно добавить фильтрацию по текущему пользователю
        if self.request.user.is_authenticated:
            queryset = queryset.filter(author=self.request.user)
        return queryset