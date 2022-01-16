"""
Author: Atahan Kucuk
Assignment: 2.5 Fluid Mechanics
Date: 09/18/2021

Description:
    This an application to measure fluid mechinacis given the user input


"""


def main():

# getting the user input 
    temperature = float(input('Enter the temperature in°C as 5, 10, or 15: '))
    vel = float(input('Enter the velocity of water in the pipe: '))
    diameter = float(input("Enter the pipe's diameter: "))


 # condition test 
    if temperature == 5: 
        viscosity = 0.00000149
    elif temperature == 10:
        viscosity = 0.00000131
    elif temperature == 15:
        viscosity = 0.00000115
# calculation
    re = float((vel * diameter ) / viscosity)

#informing the user
    print(f'At {temperature:.1f}°C, the Reynolds number for flow at {vel:.1f} m/s in a {diameter:.1f} m diameter pipe is {re:.2e}.')



if __name__ == '__main__':
    main()
