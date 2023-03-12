# Generated by Django 4.1.7 on 2023-03-12 19:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titel', models.CharField(max_length=128)),
                ('category', models.CharField(choices=[('SF', 'Sci Fi'), ('D', 'Drama'), ('AV', 'Adventure'), ('C', 'Comedy'), ('A', 'Action'), ('O', 'Other')], default='O', max_length=2)),
                ('description', models.TextField()),
                ('year', models.PositiveSmallIntegerField(default='2000')),
                ('premiere', models.DateField()),
                ('imdb_rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('director', models.CharField(max_length=256)),
            ],
        ),
    ]
