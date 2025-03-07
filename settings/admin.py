from django.contrib import admin
from .models import FileRecord, Setting


@admin.register(FileRecord)
class FileRecordAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date", "created_at")
    search_fields = ("title", "category")
    list_filter = ("category", "date", "created_at")


admin.site.register(Setting)

