# Generated by Django 2.2.6 on 2019-11-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='Phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='database',
            name='Zip',
            field=models.IntegerField(),
        ),
    ]
