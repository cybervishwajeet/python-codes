def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

number = int(input("Enter a 5-digit positive integer number: "))

if 10000 <= number <= 99999:
    print("Sum of digits:", sum_of_digits(number))
else:
    print("Please input a 5-digit number.")
