# Generated by Django 4.2.4 on 2023-10-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0008_category_img_subcategory_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
