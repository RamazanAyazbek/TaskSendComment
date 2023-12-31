# Generated by Django 4.2.6 on 2023-10-11 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_review_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='modified_by_admin',
            field=models.BooleanField(default=False, verbose_name='Изменено администратором'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Сообщение'),
        ),
    ]
