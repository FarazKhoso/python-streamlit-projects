# Write a function that takes a list of numbers and returns the sum of those numbers.

def main(list:list):
    sum_of_list = sum(list)
    return sum_of_list



if __name__ == '__main__':
   result = main([1,2,3,4,5,6,7,8])
   print(result)