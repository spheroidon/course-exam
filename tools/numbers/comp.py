def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]
