# Generated by Django 4.2.6 on 2023-10-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='review_photos/', verbose_name='Фото'),
        ),
    ]