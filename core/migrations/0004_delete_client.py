# Generated by Django 4.2.16 on 2024-11-10 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_client_remove_churndata_user_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="Client",),
    ]
