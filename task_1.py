from datetime import datetime, timedelta

def get_days_from_today(date):
    """
    Calculate the number of days between a given date and today.

    Args:
    date (str): A date string in the format 'YYYY-MM-DD'.

    Returns:
    int: The number of days between the input date and today.
         Positive if the input date is in the past, negative if it's in the future.
    str: 'Invalid date format' if the input cannot be parsed as a valid date.

    Raises:
    ValueError: If the input date string cannot be parsed.
    """
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.now()
        detla = today - date
        return int(detla.days)
    except ValueError:
        return "Invalid date format"

while True:
    choice = input("Press Enter to continue or write 'exit' to quit: ")
    if choice == "exit":
        break

    date_input = input("Enter date in format YYYY-MM-DD: ")
    print(get_days_from_today(date_input))