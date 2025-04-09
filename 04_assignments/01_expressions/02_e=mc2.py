

def calculate_energy(mass):
    C = 299792458
    energy = mass * (C**2)
    return energy 


def main():
    while True:
        mass = float(input("Enter mass in kilogram (or 0 to exit): "))
        if mass == 0 :
            break
        else:
            energy = calculate_energy(mass)
            print(f"Energy {energy} joules")    



if __name__ == '__main__':
    main()