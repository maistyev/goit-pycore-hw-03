import random

def get_numbers_ticket(min, max, quantity):
    """
    Generate a specified quantity of unique random numbers within a given range.

    Args:
    min (int): The minimum value for the random numbers (inclusive).
    max (int): The maximum value for the random numbers (inclusive).
    quantity (int): The number of unique random numbers to generate.

    Returns:
    list: A sorted list of unique random integers within the specified range.
          Returns an empty list if the input parameters are invalid.
    """

    result = []
    count = quantity

    if (min >= 1 and max <= 1000 and quantity > 0 and 
        quantity <= max_from_user - min_from_user):
        while count > 0:
            number = random.randint(min, max)
            if number not in result:
                result.append(number)
                count -= 1

    return sorted(result)

while True:
    choice = input("Press Enter to continue or write 'exit' to quit: ")

    if choice == "exit":
        break

    try:
        min_from_user = int(input("Enter minimal number (bigger than 0): "))
        max_from_user = int(input("Enter maximal number (less than 1001): "))
        quantity = int(input("Enter quantity of numbers: "))
    except ValueError:
        print("Invalid input. Please enter only integers.")
        exit()

    lottery_numbers = get_numbers_ticket(min_from_user, max_from_user, quantity)
    
    if lottery_numbers:
        print("Your winning tickets:", lottery_numbers)
    else: 
        print("Invalid parameters. Please try again.")