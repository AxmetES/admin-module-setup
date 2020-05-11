# Generated by Django 2.2.4 on 2020-05-11 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0037_auto_20200511_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owned_flat',
            field=models.ManyToManyField(blank=True, null=True, related_name='by_flats', to='property.Flat', verbose_name='Квартиры владельца'),
        ),
    ]
