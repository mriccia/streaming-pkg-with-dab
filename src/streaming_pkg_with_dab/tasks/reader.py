from functools import cached_property

from pyspark.sql import SparkSession

from streaming_pkg_with_dab.common import Task
from streaming_pkg_with_dab.config import DefaultConfig


class Reader(Task):

    @cached_property
    def spark(self) -> SparkSession:
        return SparkSession.builder.getOrCreate()

    def launch(self):
        reader = (
            self.spark.readStream.format("kafka")
            .option("kafka.bootstrap.servers", self.cfg.kafka.bootstrap_servers)
            .option("subscribe", self.cfg.kafka.topic)
            .option("startingOffsets", "earliest")
            .load()
        )
        query = (
            reader.writeStream.option("checkpointLocation", self.cfg.reader.checkpoint_location)
            .trigger(processingTime="5 seconds")
            .toTable("events", format="delta")
        )
        query.awaitTermination(self.cfg.reader.timeout)


def entrypoint():
    Reader(cfg=DefaultConfig()).launch()
