# Generated by Django 2.2.15 on 2020-11-24 06:44

from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assignments", "0015_assignmentvote_delegated_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="assignmentpoll",
            name="db_amount_global_yes",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                default=Decimal("0"),
                max_digits=15,
                null=True,
                validators=[django.core.validators.MinValueValidator(Decimal("-2"))],
            ),
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="global_yes",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="assignmentpoll",
            name="pollmethod",
            field=models.CharField(
                choices=[
                    ("votes", "Yes per candidate"),
                    ("N", "No per candidate"),
                    ("YN", "Yes/No per candidate"),
                    ("YNA", "Yes/No/Abstain per candidate"),
                ],
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="assignmentpoll",
            name="onehundred_percent_base",
            field=models.CharField(
                choices=[
                    ("YN", "Yes/No per candidate"),
                    ("YNA", "Yes/No/Abstain per candidate"),
                    ("Y", "Sum of votes including general No/Abstain"),
                    ("valid", "All valid ballots"),
                    ("cast", "All casted ballots"),
                    ("disabled", "Disabled (no percents)"),
                ],
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="assignmentpoll",
            name="pollmethod",
            field=models.CharField(
                choices=[
                    ("Y", "Yes per candidate"),
                    ("N", "No per candidate"),
                    ("YN", "Yes/No per candidate"),
                    ("YNA", "Yes/No/Abstain per candidate"),
                ],
                max_length=5,
            ),
        ),
    ]
