class Reminder:

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Argument 'name' not passed as a string.")
        if len(name) == 0:
            raise Exception("Argument 'name' passed as an empty string.")
        self.name = name
        self.all_tasks = []
        self.is_list_new = True

    def add(self, task):
        if not isinstance(task, str):
            raise Exception("Argument 'task' not passed as a string.")
        if len(task) == 0:
            raise Exception("Argument 'task' passed as an empty string.")
        self.all_tasks.append(task)
        if self.is_list_new == True:
            self.is_list_new = False

    def see_all_tasks(self):
        if len(self.all_tasks) > 0:
            return f"{self.name}'s TODO List\n" + "\n".join(self.all_tasks)
        else:
            if self.is_list_new:
                return f"{self.name}'s TODO List\nNo tasks added yet"
            else:
                return f"{self.name}'s TODO List\nAll previous tasks have been completed"
        
    def completed_task(self, task):
        if not isinstance(task, str):
            raise Exception("The argument 'task' was not passed in as a string.")
        if task in self.all_tasks:
            self.all_tasks.remove(task)
        else:
            raise Exception("The argument 'task' passed in was not found in the task list.")
        return f"Well done, {self.name}. This completed task has been removed from your list."