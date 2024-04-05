from kafka import KafkaProducer
from loguru import logger

from streaming_pkg_with_dab.common import Task
from streaming_pkg_with_dab.config import DefaultConfig


class Writer(Task):

    def launch(self):
        self.pipe()

    def pipe(self):
        logger.info("Starting writer with config: {}", self.cfg.kafka)
        producer = KafkaProducer(bootstrap_servers=self.cfg.kafka.bootstrap_servers)
        producer.send(self.cfg.kafka.topic, value=b"test message")


def entrypoint():
    Writer(cfg=DefaultConfig()).launch()
