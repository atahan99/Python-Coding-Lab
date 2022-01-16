"""
Author: Atahan Kucuk
Assignment: 08.2 - Phone Number Converter
Date: 11/7/2021


Description:
    This is an application that converts letters in phone numbers to actual phone number


"""

def convert_number(user):

    string=""
    # spliting the sentence based on "-"
    ls=user.split("-")
    for i in ls:
        if(i.isdigit()):
            string=string+i
        else:
            for j in i:
                if(j=="A" or j=="a" or j=="B" or j=="b" or j=="C" or j=="c" or j=="2" ):
                    string=string+"2"
                elif(j=="D" or j=="d" or j=="E" or j=="e" or j=="F" or j=="f" or j=="3" ):
                    string=string+"3"   
                elif(j=="G" or j=="g" or j=="H" or j=="h" or j=="I" or j=="i" or j=="4"):
                    string=string+"4"
                elif(j=="J" or j=="j" or j=="K" or j=="k" or j=="L" or j=="l" or j=="5"):
                    string=string+"5"
                elif(j=="M" or j=="m" or j=="N" or j=="n" or j=="O" or j=="o" or j=="6"):
                    string=string+"6"
                elif(j=="P" or j=="p" or j=="Q" or j=="q" or j=="R" or j=="r" or j=="S" or j=="s" or j=="7"):
                    string=string+"7"
                elif(j=="T" or j=="t" or j=="U" or j=="u" or j=="V" or j=="v" or j=="8"):
                    string=string+"8"
                elif(j=="W" or j=="w" or j=="X" or j=="x" or j=="Y" or j=="y" or j=="Z" or j=="z" or j=="9" ):
                    string=string+"9"
                elif(j=="1"):
                    string=string+"1"
                elif(j=="0"):
                    string=string+"0"

        string=string+"-"
    # Removing the last character
    string = string.rstrip(string[-1])
    return string


def main():
    #ask user input
    user = input('Enter a telephone number: ')
    
    #display the converted number
    print('The phone number is ' + convert_number(user))



if __name__ == '__main__':
    main()
