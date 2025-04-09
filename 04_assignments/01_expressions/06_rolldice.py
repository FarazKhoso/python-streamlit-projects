import random

DICE_NUMBER = 6

def main():
   first_dice = random.randint(1,DICE_NUMBER)
   second_dice = random.randint(1,DICE_NUMBER)
   total = first_dice + second_dice
   print(f"""
            First roll: {first_dice}
            First roll: {second_dice}
            Total: {total}""")

if __name__ == '__main__':  
    main()
