# Generated by Django 4.1.3 on 2023-01-16 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_airwaybill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoiceletter',
            name='quantity',
        ),
    ]