"""
Program: gathering_input.py
Author: Brandon Kerns
Last Date Modified: 1/17/24
The purpose of this program is to create a function that asks a user how many integers they would like to store into an
empty list. Next, a second function will be used to gather the integers from user input. Finally, once the user has
entered all the integers into the function, the integers will be added together, divided by the total amount, and the
average of all the integers will be displayed to the user. Additionally, unit tests will be created to ensure the
program is working as anticipated.
"""


# Create a function to prompt the user for the amount of integers they would like to store into an empty list.
def enter_total_integers():
    """
    This function will be used to gather the total amount of integers the user wishes to store.
    :return: will be a number representing the amount of integers to be stored in a list.
    """
    # Utilize a loop to gather the number, prompting the user to retry if they enter a number less than 1.
    while True:
        try:
            total = int(input("Please enter the amount of integers you would like to store: "))
            minimum = 1
            if total < minimum:
                print("You must enter at least 1 integer. Please try again.")
            else:
                break
        # Raise a ValueError exception if the user enters anything but a numerical value.
        except ValueError:
            print("You can only enter a numerical value! Try again.")
    return total


# Create a function that will be used to gather integers as input from the user, then store those integers into a list.
def get_user_integers(integers, prompt="Enter an integer: "):
    """
    This function will be used to gather the individual integers to be stored into an empty list.
    :param integers: will be the total_integers variable from the enter_total_integer function.
    :param prompt: will be a default value that is displayed to the user during each integer entry except for the last.
    :return: will be the user-inputted values contained within a list.
    """
    # Create the empty list that the integers will be appended to.
    stored_integers = []
    last = 1
    # Gather the user inputs until the entered amount is equal to the amount from enter_total_integers function.
    for i in range(integers):
        if i == integers - last:
            prompt = "Enter your last integer: "
        while i < integers:
            try:
                integer = int(input(prompt))
                stored_integers.append(integer)
                break
            except ValueError:
                print("Invalid entry! You may only enter a numerical value.")
    return stored_integers


# Create a function that will accept the list as its parameter and return the average value of the integers.
def calculate_avg(stored_integers):
    """
    This function will be used to calculate the average of the integers entered by the user.
    :param stored_integers: will be the list of integers once the user has finished entering them.
    :return: will be the calculated average of all the integers.
    """
    # Calculate the average of the numbers stored in the list by adding them together, then dividing by total amount.
    total = sum(stored_integers)
    amount = len(stored_integers)
    average = total / amount
    return average


if __name__ == "__main__":
    total_integers = enter_total_integers()
    input_integers = get_user_integers(total_integers)
    list_average = calculate_avg(input_integers)

    print(f"The list of integers is {input_integers}")
    print(f"The average of the listed integers is {list_average:.2f}")
