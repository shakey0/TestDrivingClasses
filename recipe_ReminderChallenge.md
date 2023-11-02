1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.


2. Design the Class Signature

class Reminder:
    # User-facing properties:
    #   name: string - add and see todo tasks

    def __init__(self, name):
        # Parameters:
        #   name: string representing the person's name

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   nothing
        # Side-effects
        #   Saves the task in a list in the __init__ method
        pass # No code here yet

    def see_all_tasks(self):
        # Returns:
        #   string: A formatted list of all the tasks added so far headed by a title with the user's name or saying the user hasn't added any tasks yet or saying the user has completed all tasks

    def completed_task(self, task):
        # Parameters:
        #   task: string representing a single task in the list
        # Returns:
        #   string: A message saying the task was successfully completed and removed from "name's" todo list
        # Side-effects
        #   Deletes the task in a list in the __init__ method


3. Create Examples as Tests

"""
Given a task
    adds the task to the list
    returns the formatted list
"""
angela_reminder = Reminder("Angela")
angela_reminder.add("Pick some blackberries")
angela_reminder.see_all_tasks() # => "Angela's TODO List\nPick some blackberries"
"""
Given no tasks
    returns the formatted list saying there are no tasks added yet
Given 1 task
    adds the task to the list
    returns the formatted list with 1 task
Given another task
    adds the task to the list
    returns the formatted list with 2 tasks
"""
sally_reminder = Reminder("Sally")
sally_reminder.see_all_tasks() # => "Sally's TODO List\nNo tasks added yet"
sally_reminder.add("Pick some blackberries")
sally_reminder.see_all_tasks() # => "Sally's TODO List\nPick some blackberries"
sally_reminder.add("Go shopping")
sally_reminder.see_all_tasks() # => "Sally's TODO List\nPick some blackberries\nGo shopping"
"""
Given an empty string for name
    raises an exception
"""
david_reminder = Reminder("") # raises an error with the message "Argument 'name' passed as an empty string."
"""
Given a name with a non string value
    raises an exception
"""
david_reminder = Reminder(3) # raises an error with the message "Argument 'name' not passed as a string."
"""
Given an empty string for task
    raises an exception
"""
john_reminder = Reminder("John")
john_reminder.add("") # raises an error with the message "Argument 'task' passed as an empty string."
"""
Given a task with a non string value
    raises an exception
"""
john_reminder = Reminder("John")
john_reminder.add(4) # raises an error with the message "Argument 'task' not passed as a string."
"""
Given 3 tasks
    returns the formatted list with 3 tasks
After completing a task
    returns the formatted list with 2 tasks
After completing a task
    returns the formatted list with 1 tasks
After completing a task
    returns the formatted list saying all previous tasks have been completed
"""
james_reminder = Reminder("James")
james_reminder.add("Hoover the bedrooms")
james_reminder.add("Fix the bathroom door handle")
james_reminder.add("Change the kitchen light bulb")
james_reminder.see_all_tasks() # => "James's TODO List\nHoover the bedrooms\nFix the bathroom door handle\nChange the kitchen light bulb"
james_reminder.completed_task("Fix the bathroom door handle") # => "Well done, James. This completed task has been removed from your list."
james_reminder.see_all_tasks() # => "James's TODO List\nHoover the bedrooms\nChange the kitchen light bulb"
james_reminder.completed_task("Change the kitchen light bulb") # => "Well done, James. This completed task has been removed from your list."
james_reminder.see_all_tasks() # => "James's TODO List\nHoover the bedrooms"
james_reminder.completed_task("Hoover the bedrooms") # => "Well done, James. This completed task has been removed from your list."
james_reminder.see_all_tasks() # => "James's TODO List\nAll previous tasks have been completed"
"""
Final flow check
"""
katie_reminder = Reminder("Katie")
katie_reminder.see_all_tasks() # => "Katie's TODO List\nNo tasks added yet"
katie_reminder.add("Book train to Cardiff")
katie_reminder.see_all_tasks() # => "Katie's TODO List\nBook train to Cardiff"
katie_reminder.add("Take old bed to the dump")
katie_reminder.see_all_tasks() # => "Katie's TODO List\nBook train to Cardiff\nTake old bed to the dump"
katie_reminder.completed_task("Book train to Cardiff")
katie_reminder.completed_task("Take old bed to the dump")
katie_reminder.see_all_tasks() # => "Katie's TODO List\nAll previous tasks have been completed"
"""
Given a completed task not in the list or added before
    raises an exception
"""
connie_reminder = Reminder("Connie")
connie_reminder.completed_task("Hoover the bedrooms") # raises an error with the message "The argument 'task' passed in was not found in the task list."
"""
Given a completed task not in the list or added before
    raises an exception
"""
sophie_reminder = Reminder("Sophie")
sophie_reminder.add("Fix the bathroom door handle")
sophie_reminder.completed_task("Hoover the bedrooms") # raises an error with the message "The argument 'task' passed in was not found in the task list."
"""
Given a completed task with a non string value
    raises an exception
"""
peter_reminder = Reminder("Peter")
peter_reminder.completed_task(["Book flights to Svalbard"]) # raises an error with the message "The argument 'task' was not passed in as a string."
