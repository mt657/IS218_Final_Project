# operations/base_operation.py
from abc import ABC, abstractmethod

class BaseOperation(ABC):
    """
    Base class for all mathematical operations.
    All specific operation classes must implement the calculate method.
    """

    @abstractmethod
    def calculate(operand1, operand2):
        """
        Perform the operation on operand1 and operand2.
        
        Args:
        operand1 (float): First operand for the operation.
        operand2 (float): Second operand for the operation.
        
        Returns:
        float: The result of the operation.
        """
        pass
