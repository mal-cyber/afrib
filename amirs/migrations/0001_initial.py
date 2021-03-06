# Generated by Django 3.1.2 on 2020-12-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='main_amirs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='premiers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.IntegerField(max_length=15)),
                ('reg_no', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_num', models.CharField(max_length=4)),
            ],
        ),
    ]
