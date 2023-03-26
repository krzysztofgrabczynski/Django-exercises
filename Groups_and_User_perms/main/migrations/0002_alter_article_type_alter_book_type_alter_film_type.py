# Generated by Django 4.1.7 on 2023-03-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.IntegerField(choices=[(1, 'Film'), (2, 'Book'), (3, 'Article')], max_length=7),
        ),
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.IntegerField(choices=[(1, 'Film'), (2, 'Book'), (3, 'Article')], max_length=7),
        ),
        migrations.AlterField(
            model_name='film',
            name='type',
            field=models.IntegerField(choices=[(1, 'Film'), (2, 'Book'), (3, 'Article')], max_length=7),
        ),
    ]
