from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    UserInfoViewSet,
    ShootingRecordViewSet,
    FitnessRecordViewSet,
    EducationRecordViewSet,
    LeaderOpinionRecordViewSet,
    GiftRecordViewSet,
    DisciplineRecordViewSet,
    VacationNotesViewSet,
    EltemasRecordViewSet,
    Statistics,
    DeleteRecords,
    Vacation,
    CourseViewSet,
    PreviousPositionViewSet,
    PreviousUnitViewSet,
    MedicalSituationViewSet,
    UsersName,
    FitnessShow,
    EducationsShow,
    Tesing,
    Reports
)

router = DefaultRouter()
router.register(r"userinfo", UserInfoViewSet)
router.register(r"shooting-records", ShootingRecordViewSet)
router.register(r"fitness-records", FitnessRecordViewSet)
router.register(r"education-records", EducationRecordViewSet)
router.register(r"leader-opinion-records", LeaderOpinionRecordViewSet)
router.register(r"gift-records", GiftRecordViewSet)
router.register(r"discipline-records", DisciplineRecordViewSet)
router.register(r"vacation-notes", VacationNotesViewSet)
router.register(r"eltemas-records", EltemasRecordViewSet)
router.register(r"courses", CourseViewSet)
router.register(r"previous-positions", PreviousPositionViewSet)
router.register(r"previous-units", PreviousUnitViewSet)
router.register(r'medical-situations', MedicalSituationViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("delete-records/", DeleteRecords.as_view()),
    path("statistics/", Statistics.as_view()),
    path("vacation/", Vacation.as_view()),
    path("fitness-show/", FitnessShow.as_view()),
    path("education-show/", EducationsShow.as_view()),
    path("users-name/", UsersName.as_view()),
    path("testing/", Tesing.as_view()),
    path("reports/", Reports.as_view()),
]
