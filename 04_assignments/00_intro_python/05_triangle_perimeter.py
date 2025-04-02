 # Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

def main():
    perimeter = 0
    for i in range(1,4):
        user_input = float(input(f"What is the length of side {i}?: "))
        perimeter += user_input

        print(f"The perimete of the triangle is {perimeter}")

if __name__ == '__main__':
    main()