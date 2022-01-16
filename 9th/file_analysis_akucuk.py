"""
Author: Atahan Kucuk
Assignment: 9.4 - File Analysis
Date: 11/22/2021

Description:
   This is an application that analysis the content of 2 input files in order to compare their contents. This app will sort out the content of the files and will find the common and non common words.


"""

import string
def word_count(file_name):
   word_dict = dict()
   with open(file_name) as f_in: 
        for line in f_in.readlines(): #read line by line
            for word in line.split(): #Loop word by word
                w = word.strip(string.punctuation).lower() 
                word_dict[w] = word_dict.get(w, 0) + 1 
   return word_dict 

def main(): 
   #call word_count function for both the files
   xian1_words = word_count("xian_1.txt")
   xian2_words = word_count("xian_2.txt")

   #write to xian_1_word_frequency in a sorted way
   with open("xian_1_word_frequency.txt", "a+") as f_out:
      for key in sorted(xian1_words):
         f_out.write(key+": "+str(xian1_words[key])+"\n")

   # write to xian_2_word_frequency in a sorted way
   with open("xian_2_word_frequency.txt", "a+") as f_out:
      for key in sorted(xian2_words):
         f_out.write(key+": "+str(xian2_words[key])+"\n")

   #Find common words in both sets and write it to the file
   common_words = list(set(xian1_words.keys()) & set(xian2_words.keys()))
   with open("common_words.txt", "a+") as f_out:
      for word in common_words:
         f_out.write(word+"\n")

   #Find all words in both sets and ignore the words in "common_words" list to find eitherbutnotboth
   
   eitherbutnotboth = [x for x in list(set(xian1_words.keys()).union(set(xian2_words.keys()))) if x not in common_words]
   with open("eitherbutnotboth.txt", "a+") as f_out:
      for word in eitherbutnotboth:
         f_out.write(word+"\n")


if __name__ == '__main__':
    main()
