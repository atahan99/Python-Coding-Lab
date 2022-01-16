"""
Author: Atahan Kucuk
Assignment: 04.1 - Falling
Date: 10/04/2021

Description:
    This is an application to calculate the distance travelled by and item due to the gravitational force


"""



#distance calculation
def falling_dist(time):

 distance = 0.5 * 8.87 * (time*time)
 return distance


def main():

#Displaying the output 
 print('Time (s)  Distance (m)')
 print('----------------------')
 for i in range(5,55,5):
     #formatting the output
    print(f'{i:8.0f}    {falling_dist(i):10.1f}')
    
 



if __name__ == '__main__':
    main()
