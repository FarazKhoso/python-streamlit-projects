# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

def main(list):
    double_list = []
    for element in list:
        double_list.append(element * 2)
    print(double_list)

if __name__ == '__main__':
    main([1,2,3,4,5])