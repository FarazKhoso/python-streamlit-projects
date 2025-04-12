def shorten_list(lst):
    max_length = 3
    while len(lst) > max_length:
        remove_item = lst.pop()
        print(remove_item)

def main():
    name_list : list = ["faraz","jawad","arsalan","ahsan","faisal"]
    shorten_list(name_list)

if __name__ == '__main__':
    main()
