# Generated by Django 3.2.18 on 2023-03-02 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='group_size',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
