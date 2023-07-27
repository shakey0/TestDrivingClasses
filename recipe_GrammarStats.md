1. Describe the Problem
A class that tests and stores texts for correct grammar (starting with a capital letter and ending with a fullstop)


2. Design the Class Signature
Include the name of the class, its methods with their parameters, return values, and side effects.

class GrammarStats:

    def __init__(self):
        pass
    
    def check(self, text):
        Parameters:
            text: a text containing a sentence
        Returns:
            bool: True if the sentence starts and ends with a capital letter, otherwise False

    def percentage_good(self):
        Returns:
            int: the percentage of checks that have been True so far


3. Create Examples as Tests
Make a list of examples of what the function will take and return.

# EXAMPLE

Testing for starting capital and ending punctuation mark is correct:
    Initialise class:
        check_grammar = GrammarStats()
    Call methods:
        check_grammar.check("It's a lovely day.") => True
        check_grammar.check(" Will it rain today? ") => True
        check_grammar.check("How are you today? ") => True
        check_grammar.check(" The cat is crazy!") => True
    
Testing for lowercase start and/or missing correct puncuation mark at end:
    Initialise class:
        check_grammar = GrammarStats()
    Call methods:
        check_grammar.check("my house is very nice.") => False
        check_grammar.check(" Alice needs to ask a question ") => False
        check_grammar.check(" finland is very cold.") => False
        check_grammar.check("!The cat is crazy!") => False
        check_grammar.check("This sentence wasn't finished,") => False
        check_grammar.check("katie can't click: ") => False

Testing for 100% in 1 case:
    Initialise class:
        check_grammar = GrammarStats()
    Call methods:
        check_grammar.check("It's a lovely day.") => True
        check_grammar.percentage_good() => 100

Testing for 100% in 2 cases:
    Initialise class:
        check_grammar = GrammarStats()
    Call methods:
        check_grammar.check("It's a lovely day.") => True
        check_grammar.percentage_good() => 100
        check_grammar.check(" Will it rain today? ") => True
        check_grammar.percentage_good() => 100

Testing for 50% in 2 cases:
    Initialise class:
        check_grammar = GrammarStats()
    Call methods:
        check_grammar.check("It's a lovely day.") => True
        check_grammar.percentage_good() => 100
        check_grammar.check(" will it rain today? ") => False
        check_grammar.percentage_good() => 50

Testing for 67% in 3 cases:
    Initialise class:
        check_grammar = GrammarStats()
    Call methods:
        check_grammar.check("It's a lovely day.") => True
        check_grammar.check(" will it rain today? ") => False
        check_grammar.percentage_good() => 50
        check_grammar.check("How are you today? ") => True
        check_grammar.percentage_good() => 67

Testing for 60% in 5 cases:
    Initialise class:
        check_grammar = GrammarStats()
    Call methods:
        check_grammar.check(" will it rain today? ") => False
        check_grammar.check(" Will it rain today? ") => True
        check_grammar.check("How are you today? ") => True
        check_grammar.check("This sentence wasn't finished,") => False
        check_grammar.check(" The cat is crazy!") => True
        check_grammar.percentage_good() => 60