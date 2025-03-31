from abc import ABC, abstractmethod

class DatabaseManager(ABC):
    @abstractmethod
    def load_all():
        pass

    @abstractmethod
    def save_all():
        pass
