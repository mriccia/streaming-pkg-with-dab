from abc import ABC
from dataclasses import dataclass, field


@dataclass
class Config(ABC):
    kafka: dict[str, str]


@dataclass
class DefaultConfig(Config):
    kafka: dict[str, str] = field(default_factory=lambda: {"bootstrap_servers": "localhost:9092", "topic": "events"})
