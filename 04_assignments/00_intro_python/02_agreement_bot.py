# 2. Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

def main():
    favorite_animal = input("Enter a name of your favorite animal: ")
    message = f"my favorite animal is also {favorite_animal}!"
    print(message)

if __name__ == '__main__':
    main()