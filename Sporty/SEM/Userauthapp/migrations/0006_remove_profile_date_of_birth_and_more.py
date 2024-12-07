# Generated by Django 5.1.1 on 2024-09-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userauthapp', '0005_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default_profile.jpg', upload_to='profile_pics'),
        ),
    ]