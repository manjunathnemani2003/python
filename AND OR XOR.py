# Function to convert a number to binary
def to_binary(n):
    return bin(n)[2:]

# Function to perform binary operations
def binary_operations(num1, num2):
    # Convert numbers to binary
    bin_num1 = to_binary(num1)
    bin_num2 = to_binary(num2)

    # Perform binary operations
    or_result = num1 | num2
    xor_result = num1 ^ num2
    and_result = num1 & num2

    # Convert results to binary
    bin_or_result = to_binary(or_result)
    bin_xor_result = to_binary(xor_result)
    bin_and_result = to_binary(and_result)

    # Print the results
    print(f"Binary of {num1}: {bin_num1}")
    print(f"Binary of {num2}: {bin_num2}")
    print(f"OR operation result: {bin_or_result} (Decimal: {or_result})")
    print(f"XOR operation result: {bin_xor_result} (Decimal: {xor_result})")
    print(f"AND operation result: {bin_and_result} (Decimal: {and_result})")

# Example usage
num1 = 12
num2 = 25
binary_operations(num1, num2)
