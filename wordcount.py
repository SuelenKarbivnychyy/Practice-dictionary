import sys
import string
"""Count words in file."""

# # def word_count(file_text):
# words_count = {}

# # with open("twain.txt") as file:
# #     file_content = file.readlines()

# file_content = open("test.txt")

# for line in file_content:
#     words = line.rstrip().split(" ")

#     for word in words:
#         words_count[word] = words_count.get(word, 0) + 1            #advanced way of doing the same
#         # if word not in words_count:
#         #     words_count[word] = 1
#         # else:
#         #     words_count[word] += 1

# for key, value in words_count.items():
#     print(key, value)            

        
# # print(word_count("test.txt"))

def tokenize(filename):
    """Return a list of words from the file"""

    words_list = []

    with open(filename) as file:
        file_content = file.readlines()

        for line in file_content:
            list_of_words = line.lower().rstrip().split(" ")
            
            for word in list_of_words:
                words_list.append(word)                 
    return words_list  
    

# tokenize(filename)   


def count_words(words):
    """take in a list of strings and return a dictionary of each string and the number of times it appears in the list."""

    #pseudocode:
    #create an empty dictionary
    #create a counter starting at 1
    #loop throught the list
    #check if current word is no in the dictionary
    #if true, add the word as key and the counter as value
    #if false increase the counter and update the value 
    #return the dictionary
    #call the function

    result = {}
    # counter = 1

    for word in words:
        counter = 1
        if word not in result:
            result[word] = counter
        else:
            counter += 1
            result[word] = counter
    return result

# words = sys.argv[1]
# print(count_words(["apple", "berry", "cherry", "apple"]))                




#take in a dict of words counts and print each key and value from the dictionary
#pseudocode
#define a function
#use enumerate to iterate throught the dictionary
#print key and values for each iterartion
# call your function

def print_word_counts(word_counts):

    for key, value in word_counts.items():
        print(key, value)

# print_word_counts({'apple': 2, 'berry': 1, 'cherry': 1})  


def normalize_words(words):
    """Return a list of normalized words"""

    #create an empty list to hold the words normalized
    # iterate thorught the list of words
    # define an empty string variable
    # iterate over each letter in word
    # check if current letter isalpha (if letter is actually letter)
    # if true make the empty string += letter
    # append the string that now is holding a letter to the list
    # return the list
    # 

    normalize = []

    for word in words:
        no_ponctuation = ""

        for char in word:
            if char.isalpha():
                no_ponctuation += char
        normalize.append(no_ponctuation)

    return normalize             

    
filename = sys.argv[1]
#calling the functions with other functions as parameters

tokens = tokenize(filename)
tokens = normalize_words(tokens)
word_counts = count_words(tokens)
print_word_counts (word_counts)
