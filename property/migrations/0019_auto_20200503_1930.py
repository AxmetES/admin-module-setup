# Generated by Django 2.2.4 on 2020-05-03 16:30

import phonenumbers
from django.db import migrations


def change_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.filter(owners_phonenumber='+70000000000'):
        old_number = flat.owners_phonenumber
        number_to_change = phonenumbers.parse(old_number, 'RU')
        if phonenumbers.is_valid_number(number_to_change):
            flat.owner_phone_pure = phonenumbers.format_number(number_to_change, phonenumbers.PhoneNumberFormat.E164)
            flat.save()
        else:
            flat.owner_phone_pure = 'bad number'
            flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0018_auto_20200503_1851'),
    ]

    operations = [
        migrations.RunPython(change_phone_number),
    ]
