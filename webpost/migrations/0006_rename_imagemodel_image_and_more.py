# Generated by Django 4.1.3 on 2023-01-29 07:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webpost', '0005_category_user_homemodel_alter_imagemodel_author_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageModel',
            new_name='Image',
        ),
        migrations.RenameModel(
            old_name='User_homeModel',
            new_name='UserHome',
        ),
    ]