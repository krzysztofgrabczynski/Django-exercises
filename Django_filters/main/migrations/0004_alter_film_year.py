# Generated by Django 4.1.7 on 2023-03-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_film_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.FloatField(),
        ),
    ]
