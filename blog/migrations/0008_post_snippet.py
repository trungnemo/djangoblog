# Generated by Django 3.1.3 on 2021-09-20 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210920_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read full text', max_length=255),
        ),
    ]