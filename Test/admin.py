from django.contrib import admin
from .models import Question, Test, TestResult, Topic

# Register your models here.
admin.site.register((Question, Test, TestResult, Topic))
