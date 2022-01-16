"""
Author: Atahan Kucuk
Assignment: 04.3 - Avg Grade
Date: 10/04/2021

Description:
    This is an application to determine the average and letter grade from users score inputs.


"""
#Validating and getting the user input
def get_valid_score():
    score = float(input('Enter a score: '))
    while score < 0 or score > 100 : 
        print('  Invalid Input. Please try again.')
        score = float(input('Enter a score: '))
    return score

#Determining the letter grade
def determine_grade(score):

    if score >= 91 and score <=100 :
        grade = 'A'
    elif score < 91 and score >= 82:
        grade = 'B'
    elif score < 82 and score >= 73 :
        grade = 'C'
    elif score < 73 and score >= 64 : 
        grade = 'D'
    else: 
        grade = 'F'
    return grade
# calculating the average grade
def calc_average(total):
    
    average = (total / 5)
    return average

def main():

    grade = ''
    average , total = 0, 0
    score = []
    #running the loop for getting the user input
    for i in range(0,5):
            score= float(get_valid_score())
            grade = determine_grade(score)
            print(f'  The letter grade for {score:.1f} is ' + grade +'.')
            total+=score
    #calculating the average and determing the letter grade for the average
    
    average=calc_average(total)
    grade = determine_grade(average)
    #informing the user for the results
    print('\nResults:') 
    print(f'  The average score is {average:.2f}.')
    print(f'  The letter grade for {average:.2f} is '+ grade + '.')
    

if __name__ == '__main__':
    main()
