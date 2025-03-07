from django.db import models
import os

# Create your models here.


class FileRecord(models.Model):
    CATEGORY_CHOICES = [
        ("documents", "Documents"),
        ("files", "files"),
        ("videos", "Videos"),
        ("others", "Others"),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    file = models.FileField(upload_to="files/")
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def delete(self, *args, **kwargs):
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = FileRecord.objects.get(pk=self.pk)
            if old_instance.file and self.file.name != old_instance.file.name:
                if os.path.isfile(old_instance.file.path):
                    os.remove(old_instance.file.path)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Setting(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField(blank=True)
    image = models.ImageField(upload_to="", verbose_name="صورة", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Setting.objects.get(pk=self.pk)
            if old_instance.image and self.image.name != old_instance.image.name:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.key

