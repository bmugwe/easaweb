# Generated by Django 4.1.3 on 2022-11-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_invoiceletter_user_saved_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceletter',
            name='quantity',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]