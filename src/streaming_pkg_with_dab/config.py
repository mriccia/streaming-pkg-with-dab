from dataclasses import dataclass, field


@dataclass
class KafkaInfo:
    bootstrap_servers: str
    topic: str


@dataclass
class ReaderInfo:
    timeout: int = 10
    output_table: str = "events"
    checkpoint_location: str = "/Volumes/main/default/checkpoints"


@dataclass
class DefaultConfig:
    kafka: KafkaInfo = field(default_factory=lambda: KafkaInfo(bootstrap_servers="localhost:9092", topic="test"))
    reader: ReaderInfo = field(default_factory=ReaderInfo)
