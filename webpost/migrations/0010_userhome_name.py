# Generated by Django 4.1.3 on 2023-11-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpost', '0009_alter_userhome_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userhome',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
