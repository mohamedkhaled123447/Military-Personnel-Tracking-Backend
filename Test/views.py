from rest_framework import viewsets
from .models import Question, Test, TestResult, Topic
from .pagination import QuestionPagination
from .filters import QuestionFilter
from .serializers import (
    QuestionSerializer,
    TestSerializer,
    TestResultSerializer,
    TopicSerializer,
    TestResultCreateSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView
from openpyxl import load_workbook
import random


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = QuestionFilter
    pagination_class = QuestionPagination


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    # permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        question_ids = request.data.get("questions")

        if not question_ids:
            raise ValidationError("No questions provided")

        questions = Question.objects.filter(id__in=question_ids)

        if len(questions) != len(question_ids):
            raise ValidationError("Some questions do not exist")

        test = Test.objects.create(
            name=request.data.get("name"),
            description=request.data.get("description"),
            time=request.data.get("time"),
            target=request.data.get("target"),
        )

        test.questions.set(questions)

        serializer = self.get_serializer(test)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        test_id = kwargs.get("pk")
        try:
            test = Test.objects.get(pk=test_id)
        except Test.DoesNotExist:
            raise ValidationError("Test does not exist")

        question_ids = request.data.get("questions")
        if not question_ids:
            raise ValidationError("No questions provided")

        questions = Question.objects.filter(id__in=question_ids)
        if len(questions) != len(question_ids):
            raise ValidationError("Some questions do not exist")

        test.questions.set(questions)
        test.name = request.data.get("name")
        test.description = request.data.get("description")
        test.time = request.data.get("time")
        test.target = request.data.get("target")
        test.save()
        serializer = self.get_serializer(test)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.select_related("user", "test").only(
        "id",
        "score",
        "date_taken",
        "answers",
        "user__name",
        "user_id",
        "user__is_officer",
        "user__rank",
        "user__dgree",
        "test__name",
        "test__code",
        "test_id",
    )
    serializer_class = TestResultSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return TestResultCreateSerializer
        return TestResultSerializer

    def list(self, request, *args, **kwargs):
        id = self.request.GET.get("id")
        if id == "-1":
            return Response(self.serializer_class(self.queryset.all(), many=True).data)
        results = self.queryset.filter(user=id)
        return Response(self.serializer_class(results, many=True).data)

    # permission_classes = [IsAuthenticated]


class ResultsReport(APIView):
    def post(self, request, *args, **kwargs):
        filters = {}
        if request.data["code"]:
            filters["test_id"] = request.data["code"]
        if request.data["date"]:
            filters["date_taken"] = request.data["date"]
        if request.data["name"]:
            filters["user__name__icontains"] = request.data["name"]
        results = (
            TestResult.objects.select_related("user", "test")
            .only(
                "score",
                "date_taken",
                "user_id",
                "user__name",
                "user__is_officer",
                "test__name",
                "test_id",
            )
            .filter(**filters)
        )
        try:
            wb = load_workbook("media/test_results.xlsx")
            sheet = wb["Sheet1"]
        except FileNotFoundError as e:
            return Response("File not found", status=404)
        
        for index, result in enumerate(results):
            sheet.append(
                (
                    index + 1,
                    result.user.name,
                    result.test.name,
                    result.score,
                    result.date_taken,
                )
            )
        wb.save("media/نتائج الاختبارات.xlsx")
        wb.close()
        return Response(
            {"link": f"{request.build_absolute_uri("/")}media/نتائج الاختبارات.xlsx"}
        )


class RandomTest(APIView):
    def post(self, request, *args, **kwargs):
        topic = request.data["topic"]
        n = request.data["n"]
        print(topic, n)
        questions = Question.objects.filter(topic=topic)
        data = QuestionSerializer(questions, many=True).data
        data = random.sample(data, int(n))
        return Response(data)


class TestCode(APIView):
    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        test = Test.objects.get(code=code)
        return Response(TestSerializer(test).data)
