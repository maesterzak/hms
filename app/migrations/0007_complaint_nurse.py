# Generated by Django 4.0.6 on 2022-08-06 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_complaint_doctornote_remove_complaint_feeling_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='nurse',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
