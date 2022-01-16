"""
Author: Atahan Kucuk
Assignment: 07.2 - Number Analysis
Date: 10/31/2021

Description:
    This is an application that gathers user input for 10 numbers and analyzes them to figure out the high, low, total and average numbers. 


"""

def get_number_list():
    #Getting user input 
    list_num = []
    user = 0
    for i in range(0,10):
        user = float(input(f'  number {i+1:2.0f} of 10: '))
        #storing user input in a list
        list_num.append(user)
    return list_num

def main():

    numbers = []
    
    print('Enter 10 numbers:')
    #calling the function
    numbers = get_number_list()
    #caculating and displaying analysis
    print(f'Highest number: {max(numbers):.2f}')
    print(f'Lowest number: {min(numbers):.2f}')
    print(f'Total: {sum(numbers):.2f}')
    print(f'Average: {sum(numbers)/10:.2f}')




if __name__ == '__main__':
    main()
