# Generated by Django 3.1.1 on 2020-09-23 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200923_1140'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookLanguage',
            new_name='BookLanguageclass',
        ),
    ]