# Generated by Django 2.2.12 on 2020-05-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=60)),
                ('company_email', models.CharField(max_length=60)),
                ('job_title', models.CharField(max_length=60)),
                ('salary', models.IntegerField()),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
