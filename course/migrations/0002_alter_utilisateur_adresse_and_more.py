# Generated by Django 5.2.3 on 2025-06-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='adresse',
            field=models.CharField(default='Inconnue', max_length=255),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='date_naissance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='telephone',
            field=models.CharField(default='000000000', max_length=9),
        ),
    ]
