# operations/division.py
from operations.base_operation import BaseOperation

class Divide(BaseOperation):
    """
    Class for performing division operation.
    Inherits from BaseOperation and implements calculate method.
    """
    
    def calculate(self, operand1, operand2):
        if operand2 == 0:
            raise ValueError("Cannot divide by zero")
        return operand1 / operand2
