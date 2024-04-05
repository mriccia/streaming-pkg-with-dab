from abc import ABC
from dataclasses import dataclass, field


@dataclass
class KafkaInfo:
    bootstrap_servers: str
    topic: str


@dataclass
class Config(ABC):
    kafka: KafkaInfo


@dataclass
class DefaultConfig(Config):
    kafka: KafkaInfo = field(default_factory=lambda: KafkaInfo(bootstrap_servers="localhost:9092", topic="test"))
