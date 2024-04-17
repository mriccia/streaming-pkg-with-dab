from copy import deepcopy
from uuid import uuid4

from kafka import KafkaConsumer

from streaming_pkg_with_dab.config import DefaultConfig
from streaming_pkg_with_dab.tasks.writer import Writer


def test_writer(cfg: DefaultConfig):
    _cfg = deepcopy(cfg)

    _cfg.kafka.topic = str(uuid4())[0:8]
    w = Writer(_cfg)
    w.launch()

    test_consumer = KafkaConsumer(
        _cfg.kafka.topic,
        bootstrap_servers=_cfg.kafka.bootstrap_servers,
        group_id="test",
        auto_offset_reset="earliest",
    )

    for i in range(10):
        msg = next(test_consumer)
        assert msg.value == f"Message {i}".encode()

    test_consumer.close()
