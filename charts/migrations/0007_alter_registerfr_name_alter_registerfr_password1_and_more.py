# Generated by Django 4.2.5 on 2023-11-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0006_registerfr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerfr',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='registerfr',
            name='password1',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='registerfr',
            name='password2',
            field=models.CharField(max_length=15),
        ),
    ]
