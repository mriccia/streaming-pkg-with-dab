from functools import cached_property

from pyspark.sql import SparkSession

from streaming_pkg_with_dab.common import Task
from streaming_pkg_with_dab.config import DefaultConfig


class Reader(Task):

    @cached_property
    def spark() -> SparkSession:
        return SparkSession.builder.getOrCreate()

    def launch(self):
        reader = (
            self.spark.readStream.format("kafka")
            .option("kafka.bootstrap.servers", self.cfg.kafka["bootstrap_servers"])
            .option("subscribe", self.cfg.kafka["topic"])
            .load()
        )
        reader.writeStream.format("console").start().awaitTermination()


def entrypoint():
    Reader(cfg=DefaultConfig()).launch()
