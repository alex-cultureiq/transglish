# Generated by Django 2.1.3 on 2018-11-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentences',
            name='language',
            field=models.CharField(max_length=50),
        ),
    ]