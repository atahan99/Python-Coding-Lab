"""
Author: Atahan Kucuk
Assignment: 03.3 - Rainfall
Date: 09/23/2021

Description:
    This is an application to calculate the total rainfall and average monthly rainfaill given the user data. 


"""


def main():

    #Declaring variables
    year = int(input('Enter the number of years: '))
    monthsL = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    total, average, mcount, rain = 0, 0, 0, 0 
    month = ''
    msg = ''
    #input validation
    if year >= 1:
        #Asking user input and doing calculations 
        for i in range(1, year+1):
            print(f'  For year No. {i:.0f}')
            mcount = year * 12
            for m in range(0,12):
                month = monthsL[m]
                msg='    Enter the rainfall for ' + month + '.: '   
                rain=float(input(msg))
                while rain <0:
                    print('    Invalid input, please try again.')
                    msg='    Enter the rainfall for ' + month + '.: '
                    rain=float(input(msg))
                total+=rain
                if year > 1:
                    m=0
                    month = ''   
        average =float(total/mcount)
        #Informing the user for the results
        print(f'There are {mcount:.0f} months.')
        print(f'The total rainfall is {total:.2f} inches.')
        print(f'The monthly average rainfall is {average:.2f} inches.')
    else:
        print('Invalid input.')


 




 



if __name__ == '__main__':
    main()
