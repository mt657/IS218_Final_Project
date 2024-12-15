# operations/addition.py
from operations.base_operation import BaseOperation

class Addition(BaseOperation):
    """
    Class for performing addition operation.
    Inherits from BaseOperation and implements calculate method.
    """
    
    def calculate(self, operand1, operand2):
        return operand1 + operand2
