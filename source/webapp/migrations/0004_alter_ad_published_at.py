# Generated by Django 4.1.2 on 2023-02-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_ad_avatar_ad_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
    ]
