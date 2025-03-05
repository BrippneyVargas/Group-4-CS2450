from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    description: str
    priority: int




# class Task:
#     def __init__(self, title: str, desc: str, priority: int):
#         self.title: str = title
#         self.desc: str = desc
#         self.priority: int = priority

#         # ADD tag (optional, can have multiple tags)

#     def to_dict(self) -> dict:
#         """Convert task to a dictionary, limiting the size of the description if needed.

#         Args:
#             max_desc_length (int, optional): The maximum number of characters that can be in a description. Defaults to 30.

#         Returns:
#             dict: Dictionary containing the data of the Task.
#         """
#         # max_desc_length = 30
#         # truncated_desc = (self.desc[:max_desc_length] + "...") if len(self.desc) > max_desc_length else self.desc
#         return {"Title": self.title, "Description": self.desc, "Priority": self.priority}
