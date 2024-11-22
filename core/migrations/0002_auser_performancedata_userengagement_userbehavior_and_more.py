# Generated by Django 4.2.16 on 2024-11-08 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("location", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=10)),
                ("segment", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="PerformanceData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("response_time", models.DecimalField(decimal_places=2, max_digits=5)),
                ("error_count", models.IntegerField()),
                ("downtime", models.DurationField()),
                ("api_usage_count", models.IntegerField()),
                ("timestamp", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="UserEngagement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "click_through_rate",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "interaction_rate",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "retention_metric",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "conversion_rate",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.auser"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserBehavior",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("purchase_history", models.TextField(blank=True, null=True)),
                ("content_consumption", models.TextField(blank=True, null=True)),
                ("preferences", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.auser"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserActivity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("login_count", models.IntegerField()),
                ("last_login", models.DateTimeField()),
                ("session_duration", models.DurationField()),
                ("time_spent", models.IntegerField()),
                ("most_accessed_feature", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.auser"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventTracking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action", models.CharField(max_length=100)),
                ("timestamp", models.DateTimeField()),
                ("funnel_stage", models.CharField(max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.auser"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChurnData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("churned", models.BooleanField(default=False)),
                ("cancellation_reason", models.TextField(blank=True, null=True)),
                ("feedback", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.auser"
                    ),
                ),
            ],
        ),
    ]
