import random

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...
    def __init__(self, file): # we are taking in the param file which we will input words.txt

        file = open(file) # the variable "file" is to open that text file

        # for word in file:
        #     self.word = word
        #     print("each word", word)
        #     num_of_words += 1
        
        # print(num_of_words, " words read")

        self.words_list = self.get_list(file) # here we are assigning the self.words_list variable to the seld.get_list fucntion which returns the a list of all words 
        print(len(self.words_list), " words read") #we can get the length of that list and print out the number of words on here
        
        file.close()

    def __repr__(self):
        return f"<WordFinder in a list of {len(self.words_list)} words>"

    def get_list(self, file):
        return [word.strip() for word in file] #using comprehension to return a list for each word in file with the /n off (using .strip())
        

    def random(self):
        return random.choice(self.words_list) #as we imported the "random" library we can use this fucntion to choose a random selection from the self.words list


class SpecialWordFinder(WordFinder): # this class "SpecialWordFinder" is an extension of the WordFinder class (hence its in the params)
    def get_list(self,file): #we are changing the get_list function that exists in the WordFinder class too and altering it so it returns words that dont have a # in front of it 
        return [word.strip() for word in file if word.startswith("#")== False]