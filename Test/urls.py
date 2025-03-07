from rest_framework.routers import DefaultRouter
from .views import (
    QuestionViewSet,
    TestViewSet,
    TestResultViewSet,
    TopicViewSet,
    ResultsReport,
    RandomTest,
    TestCode
)
from django.urls import path, include

router = DefaultRouter()
router.register(r"questions", QuestionViewSet)
router.register(r"topics", TopicViewSet)
router.register(r"tests", TestViewSet)
router.register(r"results", TestResultViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("results-report", ResultsReport.as_view()),
    path("random-test", RandomTest.as_view()),
    path("test-code/", TestCode.as_view()),
]
