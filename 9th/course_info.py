"""
Author: Atahan Kucuk
Assignment: 9.3 - Course Info
Date: 11/22/2021

Description:
    this is an application that creates a nested disctionary for the course number, room , instructor,  time 


"""





def get_course_data():
   # Function to create and return a nested dictionary containing course data
   course = {'CS101' : {'room': '3004', 'instructor' : 'Django', 'time':'9:00 a.m.'}, 'CS102' : {'room' : '4501', 'instructor' : 'Idle', 'time' : '10:00 a.m.'}, 'CS103' : {'room': '6755', 'instructor' : 'Rich', 'time' : '11:00 a.m.'}, 'NT110' : {'room' : '1244', 'instructor' : 'Marshal', 'time' : '12:00 p.m.'}, 'CM241' : {'room' : '1411', 'instructor' : 'Pickle', 'time': '2:00 p.m.'}}
  
   return course



def main():

   course = get_course_data()
   course_number = input("Enter a course number: ")
  
   # check if course_number is a key in course dictionary
  
   if course_number in course:
       print("  The details for course",course_number,"are:")
       # display course details
       print("    Instructor: {}\n          Room: {}\n          Time: {}".format(course[course_number]["instructor"], course[course_number]["room"], course[course_number]["time"]))
   else: 
      
       print(" ",course_number,"is an invalid course number.")



if __name__ == '__main__':
    main()
