"""
Author: Atahan Kucuk
Assignment: 08.1 - Pig Latin
Date: 11/04/2021

Description:
    This is an application that gets user input and moves the first letter to the end and adds ay at the end


"""




def pig (user): 


    #Split into words
    split = user.split()
    ans = []
    #loop through words
    for word in split:
        #Check if first letter is supper
        upper = word[0].isupper()
        #remove the first and add it at the end. Add 'ay' at the end
        sub = word[1:]+word[0].lower()+'ay'
        #f first letter is upper, convert first letter to upper in pig latin
        if upper:
            sub = sub[0].upper()+sub[1:]
        ans.append(sub)
    #Convert list to string
    return ' '.join(ans)
    


def main():
    #ask user input 
    user = input("Enter a string: ")
    #generate pig latin
    final = pig(user)
    print("Pig latin: " + final)




if __name__ == '__main__':
    main()
