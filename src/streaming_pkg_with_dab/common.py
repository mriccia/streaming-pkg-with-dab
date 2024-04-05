from abc import ABC, abstractmethod


class Task(ABC):

    @abstractmethod
    def launch(self):
        pass
