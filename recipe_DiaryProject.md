1. Describe the Problem
A class that stores the title and contents of a text


2. Design the Class Signature
Include the name of the class, its methods with their parameters, return values, and side effects.

class DiaryEntry:

    def __init__(self, title, contents):

        Parameters:
            title: a string containing the title
            contents: a text containing the contents

        Returns:
            nothing
    
    def format(self):

        Returns:
            a string in the form of a formatted diary entry with the title followed by the text

    def count_words(self):

        Returns:
            an int of the number of words in the diary

    def reading_times(self, wpm):
        
        Parameters:
            wpm: an integer representing the number of words the user can read per minute

        Returns:
            an int representing how many minutes it will take for the user to read the text
        
    def reading_chunk(self, wpm, minutes):

        Parameters:
            wpm: an integer representing the number of words the user can read per minute
            minutes: an integer representing the number of minutes the user has to read
        
        Returns:
            a string with the chunk of words the user can read in the given time


3. Create Examples as Tests
Make a list of examples of what the function will take and return.

Testing for .format():
    Initialise class:
        garden_chores = DiaryEntry("Garden Chores", "You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the shed.")
        clean_the_house = DiaryEntry("Clean the House", "We need to wipe down all the surfaces in the kitchen as well as all the tables around the house, then hoover all the carpets, and finally clean the bathroom.")
    Call methods:
        garden_chores.format() => "Garden Chores: You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the shed."
        clean_the_house.format() => "Clean the House: We need to wipe down all the surfaces in the kitchen as well as all the tables around the house, then hoover all the carpets, and finally clean the bathroom."

Testing for .count_words():
    Initialise class:
        garden_chores = DiaryEntry("Garden Chores", "You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the shed.")
        clean_the_house = DiaryEntry("Clean the House", "We need to wipe down all the surfaces in the kitchen as well as all the tables around the house, then hoover all the carpets, and finally clean the bathroom.")
    Call methods:
        garden_chores.count_words() = > 35
        clean_the_house.count_words() = > 30

Testing for .reading_times(wpm):
    Initialise class:
        garden_chores = DiaryEntry("Garden Chores", "You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the shed.")
        clean_the_house = DiaryEntry("Clean the House", "We need to wipe down all the surfaces in the kitchen as well as all the tables around the house, then hoover all the carpets, and finally clean the bathroom.")
    Call methods:
        garden_chores.reading_times(5) => 7
        clean_the_house.reading_times(3) => 10
        garden_chores.reading_times(6) => 6
        clean_the_house.reading_times(4) => 8
        garden_chores.reading_times(40) => 1
        clean_the_house.reading_times(9) => 3

Testing for .reading_chunk(wpm, minutes):
    Initialise class:
        garden_chores = DiaryEntry("Garden Chores", "You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the shed.")
        clean_the_house = DiaryEntry("Clean the House", "We need to wipe down all the surfaces in the kitchen as well as all the tables around the house, then hoover all the carpets, and finally clean the bathroom.")
    Call methods:
        garden_chores.reading_times(7) => 5
        garden_chores.reading_chunk(7, 1) => "You need to cut the grass and"
        garden_chores.reading_chunk(14, 1) => "then trim the edges of the lawn, then pull out as many weeds as"
        garden_chores.reading_chunk(4, 2) => "you can from the flowerbeds, and finally trim"
        garden_chores.reading_chunk(9, 1) => "the hedges next to the shed."
        garden_chores.reading_chunk(17, 2) => "You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the"
        garden_chores.reading_chunk(17, 2) => "shed."
        garden_chores.reading_chunk(15, 3) => "You need to cut the grass and then trim the edges of the lawn, then pull out as many weeds as you can from the flowerbeds, and finally trim the hedges next to the shed."
        garden_chores.reading_chunk(3, 5) => "You need to cut the grass and then trim the edges of the lawn, then"
        clean_the_house.reading_times(8) => 4
        clean_the_house.reading_chunk(100, 7) => "We need to wipe down all the surfaces in the kitchen as well as all the tables around the house, then hoover all the carpets, and finally clean the bathroom."
        clean_the_house.reading_chunk(6, 3) => "We need to wipe down all the surfaces in the kitchen as well as all the tables around"
        clean_the_house.reading_chunk(3, 4) => "the house, then hoover all the carpets, and finally clean the bathroom."
        clean_the_house.reading_chunk(1, 1) => "We"
