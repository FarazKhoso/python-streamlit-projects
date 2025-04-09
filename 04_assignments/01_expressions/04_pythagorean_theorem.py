import math

def main():
    side_AB = float(input("Enter side AB: "))**2
    side_AC = float(input("Enter side AC: "))**2
    Tow_sides = side_AB + side_AC
    side_BC =  math.sqrt(Tow_sides)

    print(f"""
            Traingale Sides
          ____________________
          Side_AB = {side_AB}
          Side_AC = {side_AC}
          Side_BC = {side_BC} """)

if __name__ == '__main__':
    main()

