# Generated by Django 2.1 on 2019-05-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.CharField(max_length=8)),
                ('code', models.CharField(max_length=200)),
                ('full_code', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
            ],
        ),
    ]
