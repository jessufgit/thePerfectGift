# Generated by Django 2.0.1 on 2018-01-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GiftIdeasForTeachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='comment',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='gift',
            name='webAddress',
            field=models.CharField(default='', max_length=200),
        ),
    ]
