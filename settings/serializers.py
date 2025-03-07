from rest_framework import serializers
from .models import FileRecord,Setting


class FileRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileRecord
        fields = "__all__"



class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"

