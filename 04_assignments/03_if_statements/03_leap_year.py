get_year = int(input("Enter a year: "))
def main(year):
    if year % 4 == 0 and year % 100 != 0 :
        print(f"{year} is a leap year.")
    elif get_year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == '__main__':
    main(get_year)  