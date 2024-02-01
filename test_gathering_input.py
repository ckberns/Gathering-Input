"""
This file contains the unit tests for the gathering_input.py file.
"""
# Import the unittest module, the mock library to handle input, and the functions from the main() program.
import unittest
from unittest.mock import Mock
from main import enter_total_integers, get_user_integers, calculate_avg


# Create the class that inherits unittest.TestCase to be used for testing all the functions from the main().
class TestGatheringInput(unittest.TestCase):
    # Create a test for the first function, enter_total_integers.
    def test_enter_total_integers(self):
        # Mock the input function using the patch() method from the unittest.mock module.
        with unittest.mock.patch("builtins.input") as mock_input:
            # Create the mock input value that will be used for comparison in the test.
            mock_input.return_value = "3"
            # Create a variable for the function, then call the function to ensure the input matches the mock value.
            result = enter_total_integers()
            self.assertEqual(result, 3)

    # Create a test for the second function, get_user_inputs.
    def test_get_user_inputs(self):
        with unittest.mock.patch("builtins.input") as mock_input:
            # Use the side_effect attribute from the Mock module to create an iterable list for the test.
            mock_input.side_effect = ["1", "2", "3"]
            # Call the get_user_inputs() function, using a total of 3 inputs to test proper functionality.
            result = get_user_integers(3)
            self.assertEqual(result, [1, 2, 3])

    # Create a test for the final function, calculate_avg.
    def test_calculate_avg(self):
        # Create a default list that will be added together, and then divided by the total number of elements.
        test_list = [1, 2, 3, 4, 5]
        # Call the calculate_avg function, using the test_list as the parameter.
        result = calculate_avg(test_list)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
