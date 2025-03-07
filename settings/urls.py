from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import FileRecordViewSet, SettingViewSet, BackupSQLiteView,RestoreSQLiteView

router = DefaultRouter()

router.register(r"files", FileRecordViewSet)
router.register(r"settings", SettingViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("backup-sqlite/", BackupSQLiteView.as_view(), name="backup_sqlite"),
    path("restore-sqlite/", RestoreSQLiteView.as_view(), name="restore_sqlite"),
]
