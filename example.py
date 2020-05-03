import phonenumbers

old_number = '+70000000000'
number_to_change = phonenumbers.parse(old_number, 'RU')
if phonenumbers.is_valid_number(number_to_change):
    y = phonenumbers.format_number(number_to_change, phonenumbers.PhoneNumberFormat.E164)
    print(y)
else:
    print(False)
