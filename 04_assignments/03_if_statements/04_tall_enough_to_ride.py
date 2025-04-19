def main():
    while True:
        height_input = input("Enter your height: ")
        if height_input == "":
            break
        else:
            height = int(height_input)
            if height >= 50:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()