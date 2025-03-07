from django.contrib import admin

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


# Register your models here.

admin.site.register(
    (
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
)
