# Generated by Django 4.2.4 on 2023-10-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_productmodel_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='img',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
