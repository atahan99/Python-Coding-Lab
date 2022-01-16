"""
Author: Atahan Kucuk
Assignment:10.2 - Gas Prices
Date: 11/27/2021

Description:
   This is an application that analyses the content of the given text file and plots the data into a graph and saves it as pdf file. 


"""

import matplotlib.pyplot as plt


def main(): 
   
   
    x = [] 
    y = [] 
    #open the text file
    f = open("2008_Weekly_Gas_Averages.txt") 
    lines = f.readlines() 
    # Iterate through the list
    for i, k in enumerate(lines): 
        x = x + [i] 
        y = y + [float(k.strip())]
    f.close() 

    #plotting the graph 
    plt.plot(x,y) 
    plt.grid() 
    plt.xlim([0, max(x)])
    plt.xlabel("Weeks (by number)") 
    plt.ylabel("Average Price(dollars/gallon)")
    plt.title("2008 Weekly Gas Prices") 
    #saving the file 
    plt.savefig("gas_prices_akucuk.pdf") 
    

if __name__ == '__main__':
    main()
