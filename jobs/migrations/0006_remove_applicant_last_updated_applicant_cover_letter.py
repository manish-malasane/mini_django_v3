# Generated by Django 4.1.7 on 2023-04-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0005_alter_jobtitle_last_updated"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="applicant",
            name="last_updated",
        ),
        migrations.AddField(
            model_name="applicant",
            name="cover_letter",
            field=models.CharField(default=2, max_length=500),
            preserve_default=False,
        ),
    ]
