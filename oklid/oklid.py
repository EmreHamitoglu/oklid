def FirstFactorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * FirstFactorial(num - 1)

# Test the function with example inputs
print(FirstFactorial(4))  # Output: 24
print(FirstFactorial(8))  # Output: 40320