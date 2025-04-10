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
    id: int  
    title: str
    description: str
    priority: int
    tag: str

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "tag": self.tag,
        }



