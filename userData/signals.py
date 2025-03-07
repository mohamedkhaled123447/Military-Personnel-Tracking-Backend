from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserInfo
from openpyxl import load_workbook
from .utils import user_info_fields
from .serializers import UserInfoSerializer


@receiver(post_save, sender=UserInfo)
def after_record_added(sender, instance, created, **kwargs):
    if created:
        try:
            wb = load_workbook("media/records.xlsx")
            sheet = wb["Sheet1"]

            record_data = []
            data = UserInfoSerializer(instance).data
            for field in user_info_fields:
                record_data.append(data[field])

            sheet.append(record_data)
            wb.save("media/records.xlsx")

        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
