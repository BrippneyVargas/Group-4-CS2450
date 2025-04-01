from abc import ABC, abstractmethod

class DatabaseManager(ABC):
    def __init__(self) -> None:
        self.tasks = []

    @abstractmethod
    def load_tasks(self) -> None:
        pass

    @abstractmethod
    def save_tasks(self) -> None:
        pass

    @abstractmethod
    def root(self) -> dict:
        pass

    @abstractmethod
    def get_tasks(self) -> dict:
        pass

    @abstractmethod
    def get_task(self, task_id: int) -> dict:
        pass

    @abstractmethod
    def delete_task(task_id: int) -> dict:
        pass

    @abstractmethod
    def add_task(task: dict) -> dict:
        pass

    @abstractmethod
    def update_task(task_id: int, updated_task: dict) -> dict:
        pass
