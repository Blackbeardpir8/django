# Generated by Django 5.0.6 on 2024-07-13 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_student2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.RemoveField(
            model_name='student',
            name='updated_at',
        ),
    ]
