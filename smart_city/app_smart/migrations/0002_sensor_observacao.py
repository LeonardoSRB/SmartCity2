# Generated by Django 5.1.1 on 2024-10-04 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='observacao',
            field=models.TextField(blank=True),
        ),
    ]
