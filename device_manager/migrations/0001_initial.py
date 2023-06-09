# Generated by Django 4.1.2 on 2023-04-03 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("authority", models.CharField(max_length=255)),
                ("authority_email", models.EmailField(max_length=254)),
                ("authority_phone", models.CharField(max_length=15)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="CompanyManager",
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
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="device_manager.company",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Device",
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
                ("name", models.CharField(max_length=255)),
                ("model", models.CharField(max_length=255)),
                ("serial_number", models.CharField(max_length=255)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("P", "Phone"),
                            ("T", "Tablet"),
                            ("L", "Laptop"),
                            ("O", "Other"),
                        ],
                        default="Other",
                        max_length=10,
                    ),
                ),
                ("assigned_time", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Employee",
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
                    "company_managers",
                    models.ManyToManyField(
                        related_name="employees", to="device_manager.companymanager"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeviceLogInfo",
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
                ("checked_out_from", models.DateTimeField(auto_now_add=True)),
                ("checked_in_at", models.DateTimeField(blank=True, null=True)),
                ("condition", models.TextField(blank=True, null=True)),
                (
                    "checked_in_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="checked_in_by",
                        to="device_manager.employee",
                    ),
                ),
                (
                    "checked_out_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="checked_out_to",
                        to="device_manager.employee",
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="device_manager.device",
                    ),
                ),
            ],
            options={
                "ordering": ["checked_out_from", "checked_in_at"],
            },
        ),
        migrations.AddField(
            model_name="device",
            name="assigned_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="device_manager.employee",
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="device_manager.company"
            ),
        ),
        migrations.AddField(
            model_name="company",
            name="employees",
            field=models.ManyToManyField(
                related_name="companies",
                through="device_manager.CompanyManager",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
