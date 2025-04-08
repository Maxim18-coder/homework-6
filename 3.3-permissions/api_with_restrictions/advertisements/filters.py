from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter
from advertisements.models import Advertisement, AdvertisementStatusChoices

class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    date_range = DateFromToRangeFilter(field_name='created_at')
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    creator = filters.CharFilter(field_name='creator__username', lookup_expr='icontains')
    title = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['date_range', 'status', 'creator', 'title', 'description']