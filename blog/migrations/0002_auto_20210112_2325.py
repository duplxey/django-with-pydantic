# Generated by Django 3.1.5 on 2021-01-12 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=512, unique=True),
        ),
    ]
