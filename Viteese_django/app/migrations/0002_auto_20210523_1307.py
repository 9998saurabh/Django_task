# Generated by Django 3.2.3 on 2021-05-23 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='Product_and_services',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='phone_number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='related_entities',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='secondary_email_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='secondary_phone_number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='seondary_representaive_full_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]