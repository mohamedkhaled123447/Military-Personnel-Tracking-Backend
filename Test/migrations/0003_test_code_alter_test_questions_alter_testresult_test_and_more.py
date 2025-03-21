# Generated by Django 5.1 on 2025-01-22 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_alter_test_target'),
        ('userData', '0004_alter_userinfo_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='test',
            name='questions',
            field=models.ManyToManyField(related_name='questions', to='Test.question'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to='Test.test'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_results', to='userData.userinfo'),
        ),
    ]
