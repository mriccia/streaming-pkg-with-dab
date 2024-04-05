from kafka import KafkaProducer
from loguru import logger

from streaming_pkg_with_dab.common import Task


class Writer(Task):

    def launch(self):
        self.pipe()

    def pipe(self):
        bootstrap_server = self.get_bootstrap_server()
        logger.info(f"Starting kafka producer to {bootstrap_server}")
        producer = KafkaProducer(bootstrap_servers=self.get_bootstrap_server())

    def get_bootstrap_server(self):
        return "localhost:9092"


def entrypoint():
    Task().launch()
