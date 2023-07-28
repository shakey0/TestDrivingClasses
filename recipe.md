1. Describe the Problem
...


2. Design the Class Signature
Include the name of the class, its methods with their parameters, return values, and side effects.

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        #

    def remind_me_to(self, task):
        #

    def remind(self):
        #


3. Create Examples as Tests
Make a list of examples of what the function will take and return.

"""
Given ...
    ...
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given ... and (none/invalid)
    raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

