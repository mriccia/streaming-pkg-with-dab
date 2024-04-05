from abc import ABC, abstractmethod

from streaming_pkg_with_dab.config import Config


class Task(ABC):

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg

    @abstractmethod
    def launch(self):
        pass
