import random

def main():
    for i in range(10):
        number_generator = random.randint(1,100)
        print(number_generator ,end=" ")

if __name__ == "__main__":
    main()