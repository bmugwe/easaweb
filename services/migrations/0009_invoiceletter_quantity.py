# Generated by Django 4.1.3 on 2023-01-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_remove_invoiceletter_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceletter',
            name='quantity',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
    ]