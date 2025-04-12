def update_list(list,message):
    for i in range(3):
        list.append(message)

def main():
    message = input("plz enter your name: ")
    greeting_list = []
    print("before function ", greeting_list)
    update_list(greeting_list,message)
    print("after function ",greeting_list)


if __name__ == '__main__':
    main()