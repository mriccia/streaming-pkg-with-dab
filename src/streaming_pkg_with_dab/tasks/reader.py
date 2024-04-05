from functools import cached_property
from pyspark.sql import SparkSession

from streaming_pkg_with_dab.common import Task


class Reader(Task):

    @cached_property
    def spark() -> SparkSession:
        return SparkSession.builder.getOrCreate()

    def launch(self):
        pass


def entrypoint():
    Reader().launch()
