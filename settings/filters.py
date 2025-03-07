import django_filters
from .models import FileRecord


class FileRecordFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = FileRecord
        fields = ["category"]
