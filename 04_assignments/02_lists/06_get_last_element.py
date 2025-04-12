def last_element(lst):
    print(lst[-1])

def input_func(list):
    
    while True:
        user = input("Please enter any element or type 'stop' to end: ").strip()
        if user.lower() == "stop":
            break
        else:
            list.append(user)

def main():
    list = []
    input_func(list)
    if list:
        last_element(list)
    else:
        print("list is empty")

if __name__ == '__main__': 
    main()