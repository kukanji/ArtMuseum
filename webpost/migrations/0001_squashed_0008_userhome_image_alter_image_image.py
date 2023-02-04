# Generated by Django 4.1.3 on 2023-02-02 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('webpost', '0001_initial'), ('webpost', '0002_categorymodel'), ('webpost', '0003_imagemodel'), ('webpost', '0004_rename_author_id_categorymodel_author_and_more'), ('webpost', '0005_category_user_homemodel_alter_imagemodel_author_and_more'), ('webpost', '0006_rename_imagemodel_image_and_more'), ('webpost', '0007_remove_userhome_name'), ('webpost', '0008_userhome_image_alter_image_image')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description1', models.TextField()),
                ('description2', models.TextField()),
                ('language', models.IntegerField(default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description1', models.TextField()),
                ('description2', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(default=django.utils.timezone.now, upload_to='user_home')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='webpost.category')),
            ],
        ),
    ]
