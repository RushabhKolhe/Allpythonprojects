# Generated by Django 4.0.2 on 2022-02-19 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_full_name_email_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
