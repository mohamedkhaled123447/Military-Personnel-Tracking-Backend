from django.db import models
from userData.models import UserInfo
import random


class Topic(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم الموضوع")
    TARGET_CHOICES = [
        ("ضابط", "ضابط"),
        ("ضابط صف", "ضابط صف"),
        ("جندي", "جندي"),
    ]
    target = models.CharField(max_length=255, choices=TARGET_CHOICES)

    def __str__(self):
        return f"{self.id}-{self.name}"


class Question(models.Model):
    text = models.TextField()
    options = models.JSONField()
    correct_answer = models.CharField(max_length=20)
    type = models.CharField(max_length=100, default="multiple")
    topic = models.ForeignKey(Topic, related_name="questions", on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Test(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    questions = models.ManyToManyField(Question, related_name="questions")
    time = models.IntegerField(verbose_name="وقت الاختبار", default=5)
    code = models.CharField(max_length=10, default="")
    TARGET_CHOICES = [
        ("ضابط", "ضابط"),
        ("ضابط صف", "ضابط صف"),
        ("جندي", "جندي"),
    ]
    target = models.CharField(max_length=255, choices=TARGET_CHOICES, default="ضابط")

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = "".join(
                random.choices("0123456789012345678901234567890123456789", k=4)
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class TestResult(models.Model):
    user = models.ForeignKey(
        UserInfo, on_delete=models.CASCADE, related_name="user_results"
    )
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name="test_results"
    )
    score = models.FloatField()
    date_taken = models.DateField(auto_now_add=True)
    answers = models.CharField(max_length=300, default="")
