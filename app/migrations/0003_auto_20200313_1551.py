# Generated by Django 3.0.4 on 2020-03-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200313_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='info',
            field=models.CharField(max_length=30),
        ),
    ]
