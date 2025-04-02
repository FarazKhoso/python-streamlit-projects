# 3. Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!
# The equation you should use for converting from Fahrenheit to Celsius is the following:


def main():
    degree_farhenheit = int(input("Enter temperature in fahrenheit: "))

    degrees_celsius = (degree_farhenheit - 32)*5.0/90
    message = f"Temperature: {degree_farhenheit}.0F = {degrees_celsius}"

    print(message)

if __name__ == '__main__':
    main()

