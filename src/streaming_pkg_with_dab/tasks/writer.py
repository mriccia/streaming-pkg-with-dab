from kafka import KafkaProducer
from loguru import logger

from streaming_pkg_with_dab.common import Task
from streaming_pkg_with_dab.config import DefaultConfig


class Writer(Task):

    def launch(self):
        self.pipe()

    def pipe(self):
        producer = KafkaProducer(bootstrap_servers=self.cfg.kafka.bootstrap_servers)
        for i in range(10):
            producer.send(self.cfg.kafka.topic, value=f"Message {i}".encode())
            logger.info(f"Message {i} sent")


def entrypoint():
    Writer(cfg=DefaultConfig()).launch()
