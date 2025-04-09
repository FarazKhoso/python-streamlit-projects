def main():
    num1 = int(input("Please enter an integer to be divided: "))
    num2 = int(input("Please enter an integer to divide by: "))
    Quotient = num1 // num2
    reminder = num1 % num2
    print(F"""
            {num1} / {num2}
        -----------------
          Quotient = {Quotient}
          Reminder = {reminder}""")
if __name__ == '__main__':
    main()