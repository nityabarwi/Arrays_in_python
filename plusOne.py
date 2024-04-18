def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    # If all digits are 9, add a new leading digit of 1
    return [1] + digits

# Example usage:
digits1 = [1, 2, 3]
digits2 = [4, 3, 2, 1]
digits3 = [9]

print(plusOne(digits1))  # Output: [1, 2, 4]
print(plusOne(digits2))  # Output: [4, 3, 2, 2]
print(plusOne(digits3))  # Output: [1, 0]
