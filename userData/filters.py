import django_filters
from .models import UserInfo


class UserInfoFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    militeryNumber = django_filters.CharFilter(lookup_expr="icontains")
    job_classification = django_filters.CharFilter(lookup_expr="icontains")
    classification = django_filters.CharFilter(lookup_expr="icontains")
    vacation = django_filters.CharFilter(lookup_expr="icontains")
    getInDate = django_filters.DateFilter(lookup_expr="icontains")
    getOutDate = django_filters.DateFilter(lookup_expr="icontains")
    dgree = django_filters.CharFilter(lookup_expr="icontains")
    rank = django_filters.CharFilter(lookup_expr="icontains")
    fasela = django_filters.CharFilter(lookup_expr="icontains")
    saria = django_filters.CharFilter(lookup_expr="icontains")
    is_officer = django_filters.CharFilter(lookup_expr="icontains")
    is_soldier = django_filters.CharFilter(lookup_expr="icontains")
    seniority = django_filters.CharFilter(lookup_expr="icontains")
    batch = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = UserInfo
        fields = [
            "name",
            "job_classification",
            "classification",
            "militeryNumber",
            "vacation",
            "getInDate",
            "getOutDate",
            "dgree",
            "rank",
            "fasela",
            "saria",
            "is_soldier",
            "is_officer",
            "seniority",
            "batch"
        ]


class SportFilter(django_filters.FilterSet):
    user = django_filters.CharFilter()
