from pydantic import BaseModel

class Task(BaseModel):
    '''
    Class that handle details needed for each task to be added

    Attributes: 
        - title: str - title of the task
        - description: str - description of the task
        - priority: int - level of priority (1:high, 2:medium, 3:low)
        - tag: str - A tag to categorize the task
    '''
    task_id: int
    title: str
    description: str
    priority_id: int
    tag_id: int
    status_id: int
    