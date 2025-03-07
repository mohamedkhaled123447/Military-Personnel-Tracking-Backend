from rest_framework import serializers
from .models import Question, Test, TestResult, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    topic_name = serializers.CharField(source="topic.name", read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = "__all__"


class TestResultSerializer(serializers.ModelSerializer):
    test_id = serializers.IntegerField()
    test_name = serializers.CharField(source="test.name")
    test_code = serializers.CharField(source="test.code")
    user_name = serializers.CharField(source="user.name")
    is_officer = serializers.BooleanField(source="user.is_officer")
    rank = serializers.CharField(source="user.rank")
    dgree = serializers.CharField(source="user.dgree")

    class Meta:
        model = TestResult
        fields = [
            "id",
            "score",
            "date_taken",
            "answers",
            "test_name",
            "test_code",
            "test_id",
            "user_name",
            "is_officer",
            "rank",
            "dgree",
        ]
class TestResultCreateSerializer(serializers.ModelSerializer):
     class Meta:
        model = TestResult
        fields = "__all__"