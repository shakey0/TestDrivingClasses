import pytest
from lib.TaskTracker import *

def test_reminder_add_see_task():
    angela_reminder = Reminder("Angela")
    angela_reminder.add("Pick some blackberries")
    result = angela_reminder.see_all_tasks()
    assert result == "Angela's TODO List\nPick some blackberries"

def test_reminder_see_add_see_tasks():
    sally_reminder = Reminder("Sally")
    result1 = sally_reminder.see_all_tasks()
    assert result1 == "Sally's TODO List\nNo tasks added yet"
    sally_reminder.add("Pick some blackberries")
    result2 = sally_reminder.see_all_tasks()
    assert result2 == "Sally's TODO List\nPick some blackberries"
    sally_reminder.add("Go shopping")
    result3 = sally_reminder.see_all_tasks()
    assert result3 == "Sally's TODO List\nPick some blackberries\nGo shopping"

def test_reminder_emptystring_name():
    with pytest.raises(Exception) as e:
        david_reminder = Reminder("")
    error_message = str(e.value)
    assert error_message == "Argument 'name' passed as an empty string."

def test_reminder_nonstring_name():
    with pytest.raises(Exception) as e:
        david_reminder = Reminder(3)
    error_message = str(e.value)
    assert error_message == "Argument 'name' not passed as a string."

def test_reminder_emptystring_task():
    john_reminder = Reminder("John")
    with pytest.raises(Exception) as e:
        john_reminder.add("")
    error_message = str(e.value)
    assert error_message == "Argument 'task' passed as an empty string."

def test_reminder_nonstring_task():
    john_reminder = Reminder("John")
    with pytest.raises(Exception) as e:
        john_reminder.add(4)
    error_message = str(e.value)
    assert error_message == "Argument 'task' not passed as a string."

def test_reminder_remove_completed_tasks():
    james_reminder = Reminder("James")
    james_reminder.add("Hoover the bedrooms")
    james_reminder.add("Fix the bathroom door handle")
    james_reminder.add("Change the kitchen light bulb")
    result_see1 = james_reminder.see_all_tasks()
    assert result_see1 == "James's TODO List\nHoover the bedrooms\nFix the bathroom door handle\nChange the kitchen light bulb"
    result_rem1 = james_reminder.completed_task("Fix the bathroom door handle")
    assert result_rem1 == "Well done, James. This completed task has been removed from your list."
    result_see2 = james_reminder.see_all_tasks()
    assert result_see2 == "James's TODO List\nHoover the bedrooms\nChange the kitchen light bulb"
    result_rem2 = james_reminder.completed_task("Change the kitchen light bulb")
    assert result_rem2 == "Well done, James. This completed task has been removed from your list."
    result_see3 = james_reminder.see_all_tasks()
    assert result_see3 == "James's TODO List\nHoover the bedrooms"
    result_rem3 = james_reminder.completed_task("Hoover the bedrooms")
    assert result_rem3 == "Well done, James. This completed task has been removed from your list."
    result_see4 = james_reminder.see_all_tasks()
    assert result_see4 == "James's TODO List\nAll previous tasks have been completed"

def test_reminder_final_flow_check():
    katie_reminder = Reminder("Katie")
    result1 = katie_reminder.see_all_tasks()
    assert result1 == "Katie's TODO List\nNo tasks added yet"
    katie_reminder.add("Book train to Cardiff")
    result2 = katie_reminder.see_all_tasks()
    assert result2 == "Katie's TODO List\nBook train to Cardiff"
    katie_reminder.add("Take old bed to the dump")
    result3 = katie_reminder.see_all_tasks()
    assert result3 == "Katie's TODO List\nBook train to Cardiff\nTake old bed to the dump"
    katie_reminder.completed_task("Book train to Cardiff")
    katie_reminder.completed_task("Take old bed to the dump")
    result4 = katie_reminder.see_all_tasks()
    assert result4 == "Katie's TODO List\nAll previous tasks have been completed"

def test_reminder_completed_task_not_in_list():
    connie_reminder = Reminder("Connie")
    with pytest.raises(Exception) as e:
        connie_reminder.completed_task("Hoover the bedrooms")
    error_message = str(e.value)
    assert error_message == "The argument 'task' passed in was not found in the task list."

def test_reminder_completed_task_not_in_list_2():
    sophie_reminder = Reminder("Connie")
    sophie_reminder.add("Fix the bathroom door handle")
    with pytest.raises(Exception) as e:
        sophie_reminder.completed_task("Hoover the bedrooms")
    error_message = str(e.value)
    assert error_message == "The argument 'task' passed in was not found in the task list."

def test_reminder_nonstring_completed_task():
    peter_reminder = Reminder("Peter")
    with pytest.raises(Exception) as e:
        peter_reminder.completed_task(["Book flights to Svalbard"])
    error_message = str(e.value)
    assert error_message == "The argument 'task' was not passed in as a string."