def perform_operation(num1: float, num2: float, operation: str) -> float | str:
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1: First operand
        num2: Second operand
        operation: One of 'add', 'subtract', 'multiply', or 'divide'
    
    Returns:
        Result of the operation as float, or error message for division by zero
    """
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        case _:
            return "Error: Invalid operation"
        
def perform_operation(num1, num2, operation):
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