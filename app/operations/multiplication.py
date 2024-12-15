# operations/multiplication.py
from operations.base_operation import BaseOperation

class Multiply(BaseOperation):
    """
    Class for performing multiplication operation.
    Inherits from BaseOperation and implements calculate method.
    """
    
    def calculate(operand1, operand2):
        return operand1 * operand2
