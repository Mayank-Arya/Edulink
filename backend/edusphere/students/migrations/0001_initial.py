# Generated by Django 4.1.10 on 2023-09-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('mobile_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
