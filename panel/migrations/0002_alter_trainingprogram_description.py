# Generated by Django 4.2.3 on 2023-09-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingprogram',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
