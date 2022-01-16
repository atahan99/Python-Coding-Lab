"""
Author: Atahan Kucuk
Assignment: 10.4 - Sin Cos
Date: 11/22/2021

Description:
   This is an application that draws a sin and cosine wave 


"""
#importing the libaries
import matplotlib.pyplot as plt
import numpy as np

def main(): 
    #declaring the variables
    x = np.linspace(0,2*np.pi,1000)
    y1 = np.sin(x)
    y2 = np.cos(x) 


    #plotting the graph
    graph = plt.figure()
    plot = graph.add_subplot(1, 1, 1)
    plot.spines['left'].set_position('zero') 
    plot.spines['right'].set_position('zero') 
    plot.spines['bottom'].set_position('center') 
    plot.spines['top'].set_position('center') 
    #plotting the cosine and sin waves
    plt.xticks((0,0.5*np.pi,np.pi,1.5*np.pi,2*np.pi),(0,'$\pi$/2','$\pi$','3$\pi$/2','2$\pi$')) 
    plt.yticks((-1,1)) 
    plt.plot(x,y1,'r-') 
    plt.plot(x,y2,'b-') 
    #saving the figure
    plt.savefig("sin_cos_akucuk.pdf")
    plt.show() 


if __name__ == '__main__':
    main()
