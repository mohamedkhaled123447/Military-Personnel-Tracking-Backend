# Generated by Django 5.1 on 2025-01-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userData', '0003_alter_userinfo_classification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='rank',
            field=models.CharField(choices=[('لايكن', 'لايكن'), ('ملازم', 'ملازم'), ('ملازم أول', 'ملازم أول'), ('نقيب', 'نقيب'), ('رائد', 'رائد'), ('رائد اح', 'رائد اح'), ('مقدم', 'مقدم'), ('مقدم اح', 'مقدم اح'), ('عقيد', 'عقيد'), ('عقيد اح', 'عقيد اح'), ('عميد', 'عميد'), ('عميد اح', 'عميد اح'), ('لواء', 'لواء'), ('لواء اح', 'لواء اح')], default='لايكن', max_length=100, verbose_name='الرتبة'),
        ),
    ]
