# Generated by Django 5.0.1 on 2024-01-04 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_author_gender_alter_profile_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImage',
            new_name='ProfileImage',
        ),
    ]
