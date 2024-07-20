import re

def normalize_phone(phone_number):
    """
    Normalize a phone number to a standard format.

    Args:
    phone_number (str): A string containing a phone number in various formats.

    Returns:
    str: A normalized phone number starting with '+380' for Ukrainian numbers.
         Returns None if the number cannot be normalized.
    """

    # Remove all non-digit characters except '+'.
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Check if the number is valid and normalize it.
    if cleaned_number.startswith('380'):
        return '+' + cleaned_number
    elif cleaned_number.startswith('0'):
        return '+38' + cleaned_number
    elif cleaned_number.startswith('+'):
        return cleaned_number
    

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers:", sanitized_numbers)