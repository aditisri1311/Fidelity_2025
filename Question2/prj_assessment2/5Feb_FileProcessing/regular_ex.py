import re
def is_valid_phone(number):
    pattern = r"^[6-9]\d{9}$"
    return bool(re.match(pattern, number))
# Test case
phone_numbers = ["6201650742", "5123456789", "8234567890", "911234567890"]

for number in phone_numbers:
    if is_valid_phone(number):
        print(f"{number} is a valid phone number.")
    else:
        print(f"{number} is NOT a valid phone number.")
