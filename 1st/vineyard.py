"""
Author:Atahan Kucuk
Assignment: 01.1 - Vineyard
Date: 09/13/2021

Description:
    This program is a simple program to calculate the number of
    grapevines that can fit in a row.


"""


def main():

    # asking user input for the measurements in meters
    print('Enter each of the following quantities in meters.')
    S = float(input("  How much space should be between the vines? "))
    E = float(input("  How wide is the end-post assembly? "))
    R = float(input("  How long is this row? "))

    # calulating the number of grapevines that can fit in the row
    V=(R-2*E)/S
    #formatting the result
    VF=str(int(V))

    #informing the user for the results
    print('\nThis row has enough space for ',VF,' vine(s).')



if __name__ == '__main__':
    main()
