# Generated by Django 2.2.4 on 2020-05-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0024_auto_20200505_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='full_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='ФИО владельца:'),
        ),
    ]
