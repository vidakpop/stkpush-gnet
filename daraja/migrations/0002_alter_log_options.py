# Generated by Django 5.1 on 2024-08-07 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daraja', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['-date_created']},
        ),
    ]
