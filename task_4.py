from datetime import datetime, timedelta

def next_monday(day):
    """
    Calculate the date of the next Monday from a given date.

    Args:
    day (datetime): The starting date.

    Returns:
    datetime: The date of the next Monday.
    """

    days_to_monday = (7 - day.weekday()) % 7
    return day + timedelta(days=days_to_monday)

def get_upcoming_birthdays(users):
    """
    Determine upcoming birthdays and their congratulation dates.

    Args:
    users (list): A list of dictionaries, each containing 'name' and 'birthday' keys.
                  The 'birthday' should be a string in the format 'YYYY-MM-DD'.

    Returns:
    list: A list of dictionaries representing users with upcoming birthdays.
          Each dictionary contains 'name' and 'congratulation_date' keys.
    """

    upcoming_birthdays = []
    today = datetime.now().date()
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y-%m-%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year if birthday_this_year.weekday() < 5 else next_monday(birthday_this_year)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y-%m-%d")
            })

    return upcoming_birthdays

users = [
    {"name": "Ivan", "birthday": "1990-05-15"},
    {"name": "Petro", "birthday": "1995-07-22"},
    {"name": "Olena", "birthday": "1992-07-21"}
]
print(get_upcoming_birthdays(users))