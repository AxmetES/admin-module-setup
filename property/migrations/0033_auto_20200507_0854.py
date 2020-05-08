# Generated by Django 2.2.4 on 2020-05-07 05:54

from django.db import migrations


def fill_owned_flat(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(
            full_name=flat.owner,
            owner_number=flat.owners_phonenumber,
            owner_phone_pure=flat.owner_phone_pure,
        )
        owner.owned_flat.add(flat)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0032_auto_20200507_0702'),
    ]

    operations = [
        migrations.RunPython(fill_owned_flat)
    ]
