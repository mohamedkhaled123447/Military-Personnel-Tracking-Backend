from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import FileRecord, Setting
from .serializers import FileRecordSerializer, SettingSerializer
from .filters import FileRecordFilter
from django_filters.rest_framework import DjangoFilterBackend
import os
import shutil
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings


class FileRecordViewSet(viewsets.ModelViewSet):

    queryset = FileRecord.objects.all()
    serializer_class = FileRecordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FileRecordFilter
    parser_classes = [MultiPartParser, FormParser]


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer





class BackupSQLiteView(APIView):
    def post(self, request, *args, **kwargs):
        # Define the path to the SQLite database
        db_path = settings.DATABASES["default"]["NAME"]
        if not os.path.exists(db_path):
            return Response(
                {"error": "Database file not found."}, status=status.HTTP_404_NOT_FOUND
            )

        # Define the backup directory
        backup_dir = os.path.join(settings.BASE_DIR, "media")
        # Create a new backup file
        backup_file = os.path.join(backup_dir, "db.sqlite3")
        try:
            # Copy the database file to the backup location
            shutil.copy(db_path, backup_file)
            return Response(
                {"message": "Backup created successfully.", "backup_file": backup_file},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class RestoreSQLiteView(APIView):
    def post(self, request, *args, **kwargs):
        # Define the database path
        db_path = settings.DATABASES["default"]["NAME"]

        try:
            # Ensure the uploaded file exists in the request
            uploaded_file = request.data.get("file")
            if not uploaded_file:
                return Response(
                    {"error": "No file provided."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Save the uploaded file, replacing the old file
            with open(db_path, "wb") as db_file:
                for chunk in uploaded_file.chunks():
                    db_file.write(chunk)

            return Response(
                {"message": "Database restored successfully."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
