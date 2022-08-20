# Generated by Django 4.1 on 2022-08-19 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_content_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='format',
            new_name='file_format',
        ),
        migrations.AlterUniqueTogether(
            name='content',
            unique_together={('title', 'file_format')},
        ),
    ]
