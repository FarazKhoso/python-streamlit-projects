# Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old. Beth is 6 years older than Anton. Chen is 20 years older than Beth.
#  Drew is as old as Chen's age plus Anton's age. Ethan is the same age as Chen.
def main():
    Anton = 14
    Beth  = Anton + 6
    Chen = Beth + 20
    Drew = Chen + Anton
    Ethan = Chen
    print(f"""
Anton age is {Anton} years old
Beth age is {Beth} years old
Chen age is {Chen} years old
Drew age is {Drew} years old
Ethan age is {Ethan} years old""")



if __name__ == '__main__':
    main()