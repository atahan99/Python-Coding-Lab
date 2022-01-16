"""
Author: Atahan Kucuk
Assignment: 08.5 - Number Reader
Date: 11/15/2021

Description:
this is an application that reads from a previously created file that has random numbers on it and finds its min, max, sum, average and count of numbers.


"""


def main():

    #declarimng an array to store the random numbers
    lines = []
    #iterating through the file
    with open('random_numbers.txt') as fo:
        for line in fo:
            lines.append(int(line.rstrip()))
    #finding the count, min, max, sum and average of the random numbers
    countL = len(lines)
    minL = min(lines)
    maxL = max(lines)
    sumL = sum(lines)
    avgL = float(sumL / countL)

    #displaying the outputs 
    print(f'{countL:2,.0f} numbers were read from the file.')
    print(f'Min: {minL:1,.0f}')
    print(f'Max: {maxL:1,.0f}')
    print(f'Sum: {sumL:2,.0f}')
    print(f'Avg: {avgL:1,.1f}')
    fo.close



if __name__ == '__main__':
    main()
