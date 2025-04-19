country1 = 16
country2 = 25
country3 = 48

age = int(input("Enter your age: "))

if age >= country3 and age <= 80:
    print("""
        You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You can vote in Mayengua where the voting age is 48.""")
elif age >= country2 and age < country3:
    print("""
        You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.""")
elif age >= country1 and age < country2:
    print("""
        You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.""")
else:
    print("Age should between (16 to 80)")