# Generated by Django 5.1 on 2025-01-19 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userData', '0002_medicalsituation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('options', models.JSONField()),
                ('correct_answer', models.CharField(max_length=20)),
                ('type', models.CharField(default='multiple', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='اسم الموضوع')),
                ('target', models.CharField(choices=[('ضابط', 'ضابط'), ('ضابط صف', 'ضابط صف'), ('جندي', 'جندي')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('time', models.IntegerField(default=5, verbose_name='وقت الاختبار')),
                ('target', models.CharField(choices=[('ضابط', 'ضابط'), ('ضابط صف', 'ضابط صف'), ('جندي', 'جندي')], max_length=255)),
                ('questions', models.ManyToManyField(related_name='tests', to='Test.question')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('date_taken', models.DateField(auto_now_add=True)),
                ('answers', models.CharField(default='', max_length=300)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to='userData.userinfo')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='Test.topic'),
        ),
    ]
