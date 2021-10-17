"""
    Single instance to store all task data
"""

class Taskmanager():
  def __init__(self):
    self.all_data = {}
    pass
  
  def add_task (self, id, data):
    all_data = self.all_data
    all_data[id] = data
    print('Successfully add task', id, 'into manager.')
    print('Data', all_data)
    return
  
  def get_task_byid (self, id):
    all_data = self.all_data
    if all_data[id] is not None:
      return all_data[id]
    return None


task_manager = Taskmanager()