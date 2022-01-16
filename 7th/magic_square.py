"""
Author: Atahan Kucuk
Assignment: 07.4 - Magic Square
Date: 10/31/2021

Description:
    This is an application that determines if the matrix is Lo Shu magic square or not 


"""

def print_square(matrix):
    
    #print matrix 
    for i in range (3):
        print('  ', end='')
        for j in range(3):
            print(matrix[i][j],end = ' ')
        print()

def is_magic(matrix):
    j=0
    #traversing the array to check the elements
    for i in range(1,10):
        if not((i in matrix[0])or(i in matrix[1])or(i in matrix[2])):
            return False
    #calculate digonal sum
    diagtotal = 0
    for i in range(3):
        diagtotal+= matrix[i][i]

    #calulate row sum 
    for i in range(3):
        rowtotal=0
        for j in range(3):
            rowtotal+=matrix[i][j]
    # compare diagtotal and row total 
        if rowtotal != diagtotal:
            return False
    #calculate collumn sum 
    for i in range(3):
        coltotal=0
        for j in range(3):
            coltotal+=matrix[j][i]
    #compare diagtotal and coltotal
        if diagtotal != coltotal:
            return False


    return True

def main():

    #defining the matrixes
    a = [[1,2,3],[4,5,6],[7,8,9]]
    b = [[5,5,5],[5,5,5],[5,5,5]]
    c = [[4,9,2],[3,5,7],[8,1,6]]
    #print & determine status of matrix a 
    print('Your square is:')
    print_square(a)
    if is_magic(a):
        print('It is a Lo Shu magic square!')
    else:
        print('It is not a Lo Shu magic square.')
    print()
    #print & determine status of matrix b
    print('Your square is:')
    print_square(b)
    if is_magic(b):
        print('It is a Lo Shu magic square!')
    else:
        print('It is not a Lo Shu magic square.')
    print()
    #print & determine status of matrix c
    print('Your square is:')
    print_square(c)
    if is_magic(c):
        print('It is a Lo Shu magic square!')
    else:
        print('It is not a Lo Shu magic square.')
    print()
    

if __name__ == '__main__':
    main()
