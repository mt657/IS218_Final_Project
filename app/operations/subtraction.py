# operations/subtraction.py
from operations.base_operation import BaseOperation

class Subtraction(BaseOperation):
    """
    Class for performing subtraction operation.
    Inherits from BaseOperation and implements calculate method.
    """
    
    def calculate(self, operand1, operand2):
        return operand1 - operand2
