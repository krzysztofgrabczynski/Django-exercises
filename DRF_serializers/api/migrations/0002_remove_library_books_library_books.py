# Generated by Django 5.0.4 on 2024-05-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='books',
        ),
        migrations.AddField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(related_name='library', to='api.book'),
        ),
    ]
