import unittest
import sys
import os

# Ensure the app is imported correctly by adding the path to sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Importing the Flask app from app.py

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Set up the Flask test client
        self.client = app.test_client()
        self.client.testing = True

    # Test addition
    def test_addition(self):
        response = self.client.post("/basicCalculation", data={
            "num1": "5", "num2": "10", "operation1": "+"
        })
        self.assertIn(b"15.0", response.data)

    # Test subtraction
    def test_subtraction(self):
        response = self.client.post("/basicCalculation", data={
            "num1": "10", "num2": "4", "operation1": "-"
        })
        self.assertIn(b"6.0", response.data)

    # Test multiplication
    def test_multiplication(self):
        response = self.client.post("/basicCalculation", data={
            "num1": "3", "num2": "7", "operation1": "x"
        })
        self.assertIn(b"21.0", response.data)

    # Test division
    def test_division(self):
        response = self.client.post("/basicCalculation", data={
            "num1": "20", "num2": "4", "operation1": "÷"
        })
        self.assertIn(b"5.0", response.data)

    # Test division by zero
    def test_division_by_zero(self):
        response = self.client.post("/basicCalculation", data={
            "num1": "10", "num2": "0", "operation1": "÷"
        })
        self.assertIn(b"Error: Division by zero", response.data)

    # Test square root
    def test_square_root(self):
        response = self.client.post("/complexCalculation", data={
            "num3": "25", "operation2": "√"
        })
        self.assertIn(b"5.0", response.data)

    # Test square
    def test_square(self):
        response = self.client.post("/complexCalculation", data={
            "num3": "4", "operation2": " ^ 2"
        })
        self.assertIn(b"16.0", response.data)

    # Test cube
    def test_cube(self):
        response = self.client.post("/complexCalculation", data={
            "num3": "3", "operation2": " ^ 3"
        })
        self.assertIn(b"27.0", response.data)

    # Test invalid input in basic calculation
    def test_invalid_input_basic(self):
        response = self.client.post("/basicCalculation", data={
            "num1": "abc", "num2": "10", "operation1": "+"
        })
        self.assertIn(b"Invalid input", response.data)

    # Test invalid input in complex calculation
    def test_invalid_input_complex(self):
        response = self.client.post("/complexCalculation", data={
            "num3": "xyz", "operation2": " ^ 2"
        })
        self.assertIn(b"Invalid input", response.data)

if __name__ == "__main__":
    unittest.main()
