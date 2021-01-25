# Generated by Django 2.2.4 on 2019-09-04 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("marketing", "0010_auto_20190805_1038"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contactemailcampaign",
            options={"ordering": ("created_on",)},
        ),
        migrations.CreateModel(
            name="DuplicateContacts",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "contact_list",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="duplicate_contact_contact_list",
                        to="marketing.ContactList",
                    ),
                ),
                (
                    "contacts",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="duplicate_contact",
                        to="marketing.Contact",
                    ),
                ),
            ],
        ),
    ]