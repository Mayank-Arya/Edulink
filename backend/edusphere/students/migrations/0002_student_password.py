# Generated by Django 4.1.10 on 2023-09-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='your_default_password_here', max_length=128),
        ),
    ]