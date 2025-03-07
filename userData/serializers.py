from rest_framework import serializers
from Test.serializers import TestResultSerializer
from .models import (
    UserInfo,
    ShootingRecord,
    FitnessRecord,
    EducationRecord,
    LeaderOpinionRecord,
    GiftRecord,
    DisciplineRecord,
    VacationNote,
    EltemasRecord,
    Course,
    PreviousPosition,
    PreviousUnit,
    MedicalSituation,
)


class ShootingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShootingRecord
        fields = "__all__"


class FitnessRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessRecord
        fields = "__all__"


class EducationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationRecord
        fields = "__all__"


class LeaderOpinionRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeaderOpinionRecord
        fields = "__all__"


class GiftRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = GiftRecord
        fields = "__all__"


class DisciplineRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = DisciplineRecord
        fields = "__all__"


class VacationNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationNote
        fields = "__all__"


class EltemasRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = EltemasRecord
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class PreviousPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousPosition
        fields = "__all__"


class PreviousUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousUnit
        fields = "__all__"


class MedicalSituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalSituation
        fields = "__all__"


class UserInfoSerializer(serializers.ModelSerializer):
    # Using related_name in serializers for reverse relationships
    shooting_records = ShootingRecordSerializer(many=True, read_only=True)
    fitness_records = FitnessRecordSerializer(many=True, read_only=True)
    education_records = EducationRecordSerializer(many=True, read_only=True)
    leader_opinion_records = LeaderOpinionRecordSerializer(many=True, read_only=True)
    gift_records = GiftRecordSerializer(many=True, read_only=True)
    discipline_records = DisciplineRecordSerializer(many=True, read_only=True)
    eltemas_records = EltemasRecordSerializer(many=True, read_only=True)
    courses = CourseSerializer(many=True, read_only=True)
    previous_positions = PreviousPositionSerializer(many=True, read_only=True)
    previous_units = PreviousUnitSerializer(many=True, read_only=True)
    user_results = TestResultSerializer(many=True, read_only=True)
    medical_situations = MedicalSituationSerializer(many=True, read_only=True)

    class Meta:
        model = UserInfo
        fields = "__all__"
        depth = 1


class UserInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [
            "id",
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
            "batch",
            "unified_number"
        ]


class UsersNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ["id", "name", "image", "is_officer", "dgree", "rank"]
