# Generated by Django 4.2 on 2023-04-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_bookmodel_redirect_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='slug',
            field=models.SlugField(max_length=254, null=True),
        ),
    ]