from abc import ABC, abstractmethod
from Task_manager_app.src.model.Task import *
from typing import Any

class DatabaseManager(ABC):
    @abstractmethod
    def load_all(self) -> None:
        pass

    @abstractmethod
    def save_all(self) -> None:
        pass
    
    @abstractmethod
    def root(self) -> dict:
        pass

    @abstractmethod
    def get_all(self) -> dict:
        pass

    @abstractmethod
    def get(self, primary_key: Any) -> dict:
        pass

    @abstractmethod
    def delete(self, primary_key: Any) -> dict:
        pass

    @abstractmethod
    def add(item_to_add: Any) -> Any:
        pass

    @abstractmethod
    def update(primary_key: Any, updated_item: Any) -> Any:
        pass
