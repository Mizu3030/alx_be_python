from typing import Union

def perform_operation(num1: float, num2: float, operation: str) -> Union[float, str]:
    """
    Performs an arithmetic operation on two numbers.

    Supported operations:
        - 'add'
        - 'subtract'
        - 'multiply'
        - 'divide'

    Returns:
        float: Result of the operation.
        str: Error message if operation is invalid or division by zero.
    """
    operation = operation.lower()
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
