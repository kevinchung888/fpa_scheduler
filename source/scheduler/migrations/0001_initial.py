# Generated by Django 3.0.8 on 2020-07-21 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbrev', models.CharField(max_length=10)),
                ('provider_range', models.TextField()),
                ('weekend', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=50)),
                ('name_last', models.CharField(max_length=50)),
                ('abbrev', models.CharField(max_length=3)),
                ('num_work_days', models.TextField()),
            ],
        ),
    ]
