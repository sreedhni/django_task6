# Generated by Django 5.0.3 on 2024-03-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='place',
            field=models.CharField(max_length=50, null=True),
        ),
    ]