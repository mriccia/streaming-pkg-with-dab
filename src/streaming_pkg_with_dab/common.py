from abc import ABC, abstractmethod

from streaming_pkg_with_dab.config import DefaultConfig


class Task(ABC):

    def __init__(self, cfg: DefaultConfig) -> None:
        self.cfg = cfg

    @abstractmethod
    def launch(self):
        pass
