# Generated by Django 4.0.4 on 2022-06-24 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='email',
            field=models.EmailField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
