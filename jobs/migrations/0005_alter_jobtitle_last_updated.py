# Generated by Django 4.1.7 on 2023-04-07 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0004_alter_applicant_id_alter_jobdescription_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobtitle",
            name="last_updated",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
