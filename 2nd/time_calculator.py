"""
Author: Atahan Kucuk
Assignment: 02.4 - Time Calculator
Date: 09/18/2021

Description:
    It is an app to calculate the time in terms of days, hours and minutes and secons given the seconds

"""


def main():

    
    time = int(input('Please enter a time in seconds: '))
    seconds = time
    days = int(seconds / 86400)
    hours = 0
    minutes = 0
    #Calculating the time variables
    if days > 0 :
        seconds = seconds - days * 86400
        hours = int(seconds/3600)
    if hours > 0 :
        seconds = seconds - hours * 3600
        minutes = int(seconds/60)
    if minutes > 0 :
        seconds = seconds - minutes * 60

   
    
    #Informing the user
    if time < 60 :
        print(f'  {time:,.0f} seconds is less than one minute.')
    else:
        print(f'  {time:,.0f} seconds is: ',end= '')
        if days != 0 :
            print(f'{days:.0f} day(s)', end ='')
            if hours != 0 or minutes != 0 :
                print(',', end='')
        if hours !=0 :
            print(f'{hours:.0f} hours(s)', end ='')
            if minutes != 0: 
                print(',', end='')
        if minutes != 0 :
            print(f'{minutes:.0f} minutes(s)', end ='')
        if seconds != 0 : 
            print(f'{seconds:.0f}  seconds(s)', end ='')
        print('.')


    


    

    
    

 



if __name__ == '__main__':
    main()
