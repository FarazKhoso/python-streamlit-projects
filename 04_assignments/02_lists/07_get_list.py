def take_input():
    lst = []
    while True:
        user = input("Enter anything: ").strip()
        if user == "":
            break
        else:
            lst.append(user)
    print(lst)

def main():
    take_input()

if __name__ == '__main__':
    main()
