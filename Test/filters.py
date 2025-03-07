import django_filters
from .models import Question


class QuestionFilter(django_filters.FilterSet):
    topic = django_filters.CharFilter(lookup_expr="exact")

    class Meta:
        model = Question
        fields = [
            "topic",
        ]
