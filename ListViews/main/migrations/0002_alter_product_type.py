# Generated by Django 4.1.7 on 2023-04-03 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('F', 'Food'), ('E', 'Electronic'), ('C', 'Clothes'), ('B', 'Book'), ('O', 'Other')], max_length=10),
        ),
    ]
