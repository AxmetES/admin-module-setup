# Generated by Django 2.2.4 on 2020-05-07 04:02

from django.db import migrations


def fill_owners(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(full_name=flat.owner, owner_number=flat.owners_phonenumber,
                                    owner_phone_pure=flat.owner_phone_pure)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0031_owner'),
    ]

    operations = [
        migrations.RunPython(fill_owners)
    ]
