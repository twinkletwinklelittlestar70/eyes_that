"""
    Single instance to store all task data
"""

class TaskManager():
  ''' Manage and store the task data
    Taskmanager Class will store the image task data to be recognize.
  '''

  def __init__(self):
    self.all_data = {}
    pass
  
  def add_task (self, id, data):
    all_data = self.all_data
    all_data[id] = data
    print('Successfully add task', id, 'into manager.')
    # print('Data', all_data)
    return
  
  def get_task_byid (self, id):
    all_data = self.all_data
    if all_data[id] is None:
      # TODO: throw error 1001
      return None
    
    data = all_data[id]
    del all_data[id]
      
    return data

task_manager = TaskManager()