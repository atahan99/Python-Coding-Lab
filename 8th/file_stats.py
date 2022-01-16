"""
Author: Atahan Kucuk
Assignment: 08.3 - File Stats
Date: 11/04/2021

Description:
    This is an application that get a file as input and reads it 

"""


def main():
    
    #getting word count
    words = []
    with open('frontiero_v_richardson.txt') as fo:
        x = fo.read()
        words= x.split()
    fo.closed
        
    
    lines = []
    #calculating the line count
    with open('frontiero_v_richardson.txt') as fo:
        for line in fo:
            lines.append(line.rstrip())
    fo.closed

    countW = len(words)
    countL = len(lines)
    #calculating the average
    average = float(countW / countL)
    #displaying the output
    print(f'Total number of words: {countW:.0f}')
    print(f'Total number of lines: {countL:.0f}')
    print(f'Average number of words per line: {average:.1f}')
    


if __name__ == '__main__':
    main()
