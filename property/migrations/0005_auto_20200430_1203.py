# Generated by Django 2.2.4 on 2020-04-30 09:03

from django.db import migrations


def check_out_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = flat.construction_year >= 2015
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0004_auto_20200430_0626'),
    ]

    operations = [
        migrations.RunPython(check_out_new_building),
    ]
