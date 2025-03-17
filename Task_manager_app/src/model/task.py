
from fastapi import FastAPI
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
    title: str
    description: str
    priority: int
    tag: str


class AddTask(Task):
    '''
    Class inherits from Task class that handles new task to be added and auto increment the id 

    Attributes: 
        - ud: int - auto increment id for each task
        - title: str - title of the task
        - description: str - description of the task
        - priority: int - level of priority (1:high, 2:medium, 3:low)
        - tag: str - A tag to categorize the task

    '''
    id: int



