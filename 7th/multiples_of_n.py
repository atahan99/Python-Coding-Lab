"""
Author: Atahan Kucuk
Assignment: 07.1 - Multiples of N
Date: 10/25/2021

Description:
    It is an simple application that allows for finding the multiples of a given number and list 


"""


def multiples_of(num,original):
    # generating list of numbers
    list_num = []
    for i in original:
        if i % num == 0:
            list_num.append(i)
    return list_num



def main():
    #definining orginal list of numbers
    original = [19, 1599, -546, 10, 39, -58 ,1 ,85 ,201 ,-91 ,286 ,799 ,406 ]
    num = 13
    #Displaying the original list 
    print("Original list of numbers:")
    print(f'  {original}')
    list_num = multiples_of(num, original)
    #Displaying the multiples 
    print(f'Numbers in the list that are multiples of {num:.0f}:')
    print(f'  {list_num}')


if __name__ == '__main__':
    main()
