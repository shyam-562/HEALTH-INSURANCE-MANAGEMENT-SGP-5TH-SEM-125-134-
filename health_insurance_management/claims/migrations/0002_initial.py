# Generated by Django 5.0.6 on 2024-09-15 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('claims', '0001_initial'),
        ('policies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policies.policy'),
        ),
    ]
