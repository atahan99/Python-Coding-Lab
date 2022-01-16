"""
Author: Atahan Kucuk
Date: 11/22/2021

Description:
   This is an application that analysis the content of 2 input files in order to compare their contents


"""
import datetime
import numpy as np
import matplotlib.pyplot as plt


def main(): 
   
    
    f = open("indiana_covid_19_data_fall_2021.txt", "r")

    # lists for dates and positive cases
    dates = []
    pos = []

    
    for line in f:
    # split lines into words
        words = line.split(" ")
    
    # read the first word for date
    # and third word for new positive cases
        dates.append(datetime.datetime.strptime(words[0], '%Y-%m-%d').date())
        pos.append(float(words[2]))
    
    # transform the pos list to store cumulative positive cases
    pos = np.cumsum(pos)

    # plot bar graph
    plt.bar(dates, pos)
    plt.title('Positive COVID-19 Cases in Indiana')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases (in thousands)')
    plt.xticks(np.arange(dates[4], dates[-1], datetime.timedelta(days=7)), rotation=30)
    plt.yticks(np.arange(0,pos[-1],1000))
    plt.show()
    plt.savefig("covid_19_cases_akucuk.pdf")
    f.close

if __name__ == '__main__':
    main()
