# Generated by Django 4.1.7 on 2023-04-07 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicant",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="jobdescription",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="jobdescription",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="jobs.portal"
            ),
        ),
        migrations.AlterField(
            model_name="portal",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
