# Generated by Django 3.2.3 on 2021-05-22 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, null=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('User_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_business_name', models.CharField(max_length=200, null=True)),
                ('supplier_address', models.CharField(max_length=200, null=True)),
                ('representaive_full_name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Registration',
            },
        ),
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('pr_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_business_name', models.CharField(max_length=200, null=True)),
                ('supplier_address', models.CharField(max_length=200, null=True)),
                ('primary_representaive_full_name', models.CharField(max_length=200, null=True)),
                ('email_address', models.CharField(max_length=200, null=True)),
                ('phone_number', models.CharField(max_length=200, null=True)),
                ('seondary_representaive_full_name', models.CharField(max_length=200, null=True)),
                ('secondary_email_address', models.CharField(max_length=200, null=True)),
                ('secondary_phone_number', models.CharField(max_length=200, null=True)),
                ('related_entities', models.CharField(max_length=200, null=True)),
                ('Product_and_services', models.CharField(max_length=200, null=True)),
                ('User_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.registration')),
            ],
            options={
                'verbose_name_plural': 'user_data',
            },
        ),
    ]
