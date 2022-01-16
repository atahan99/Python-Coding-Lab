"""
Author: Atahan Kucuk
Assignment: 10.1 - Monthly Sales   
Date: 11/27/2021

Description:
   This is an application taht asks for user input for the monthly sales numbers and plots them on a pie chart.


"""
#importing mathplotlib
import matplotlib.pyplot as p

def main(): 
    

    #initilizate sales list
    sales = [0,0,0,0,0,0,0,0,0,0,0,0] 
    #months list
    months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] 
    #color list
    color = ["#4D4038", "#BAA892", "#5B6870", "#6E99B4", "#A3D6D7", "#085C11", "#849E2A", "#C3BE0B", "#E9E45B", "#6B4536", "#B46012", "#FF9B1A"] 

    #asking user input for the sales in each month 
    sales[0] = float(input(f"Enter the sales for {months[0]}: ")) 
    sales[1] = float(input(f"Enter the sales for {months[1]}: ")) 
    sales[2] = float(input(f"Enter the sales for {months[2]}: ")) 
    sales[3] = float(input(f"Enter the sales for {months[3]}: ")) 
    sales[4] = float(input(f"Enter the sales for {months[4]}: ")) 
    sales[5] = float(input(f"Enter the sales for {months[5]}: ")) 
    sales[6] = float(input(f"Enter the sales for {months[6]}: ")) 
    sales[7] = float(input(f"Enter the sales for {months[7]}: ")) 
    sales[8] = float(input(f"Enter the sales for {months[8]}: ")) 
    sales[9] = float(input(f"Enter the sales for {months[9]}: ")) 
    sales[10] = float(input(f"Enter the sales for {months[10]}: ")) 
    sales[11] = float(input(f"Enter the sales for {months[11]}: ")) 


    #plotting the pie chart
    p.pie(sales, colors=color, labels=months) 
    #title of the graph
    p.title("Monthly Sales Values") 
    #save as pdf
    p.savefig("monthly_sales_akucuk.pdf") 
    p.show() 

if __name__ == '__main__':
    main()
