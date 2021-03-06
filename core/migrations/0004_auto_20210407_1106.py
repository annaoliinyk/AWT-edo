# Generated by Django 2.2.13 on 2021-04-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]
