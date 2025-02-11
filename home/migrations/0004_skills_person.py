# Generated by Django 5.0.6 on 2024-07-10 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_brand_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=100)),
                ('skill', models.ManyToManyField(to='home.skills')),
            ],
        ),
    ]
