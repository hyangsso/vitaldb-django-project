# Generated by Django 4.2.1 on 2023-05-30 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinformation',
            name='sex',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
