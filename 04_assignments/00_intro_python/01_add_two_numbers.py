# 1. Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:


def main():
    num1  = int(input("Enter your first number: "))
    num2  = int(input("Enter your second number: "))
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")

if __name__ == '__main__':
    main()

