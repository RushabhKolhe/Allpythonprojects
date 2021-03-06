# Generated by Django 4.0.2 on 2022-02-25 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_email_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=300)),
                ('address2', models.CharField(default='', max_length=300)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('zip', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
    ]
