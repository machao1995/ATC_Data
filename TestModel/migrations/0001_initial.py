# Generated by Django 3.0.4 on 2020-04-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atcName', models.CharField(max_length=20)),
                ('atcSex', models.CharField(max_length=20)),
            ],
        ),
    ]