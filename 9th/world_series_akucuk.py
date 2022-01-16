"""
Author: Atahan Kucuk
Assignment: 9.2 - World Series
Date: 11/22/2021

Description:
    It is aan application that will read a file and outputs the analysis  of it. there is a fucntion that aopens and analysis the files and returns dictionaries


"""


def load_winners_data():

#read file data to list
    f=open("WorldSeriesWinners.txt",'r')
    l=list(f.readlines())
    for i in range(len(l)):
        l[i]=l[i][:-1]
    #dictionary 
    d=dict()
    c=0
    for i in range(1903,2021):
        if i==1994 or i==1904:
            continue
        #store year as key and value as country
        d[i]=l[c]
        c+=1
    d2=dict()
    for i in l:
        d2[i]=0

    for i in l:
        #store frequency
        d2[i]+=1
    f.close
    return d , d2



def main():
    
    x,y = load_winners_data()
    #read input year
    n=int(input("Enter a year in the range 1903 -- 2020: "))
    if n<1903 or n>2020:
        #print appropriate message if invalid input year
        print(f"  Data for the year {n} is not included in this system.")
    elif n==1994 or n==1904:
        print(f"  The World Series wasn't played in the year {n}.")
    else:
        #print details of country won that year
        print(f"  The {x[n]} won the World Series in {n}.")
        print(f"  They have won the World Series {y[x[n]]} times.")
   


if __name__ == '__main__':
    main()
