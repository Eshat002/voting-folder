# Generated by Django 3.2.13 on 2022-05-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_alter_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='imageA',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='question',
            name='imageB',
            field=models.ImageField(upload_to='images'),
        ),
    ]
