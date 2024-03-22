from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.streaming.query import StreamingQuery
from dataclasses import dataclass


@dataclass
class Destination:
    """Describes the destination"""

    format: str = "console"


class Task:

    @property
    def spark() -> SparkSession:
        return SparkSession.builder.getOrCreate()

    @property
    def dest() -> Destination:
        return Destination()

    def launch(self):
        source = self.get_source()
        query = self.pipe(source, self.dest)
        query.awaitTermination()

    def get_source(self) -> spark.DataFrame:
        return self.spark.readStream.format("rate").load()

    def pipe(self, source: DataFrame, dest: Destination) -> StreamingQuery:
        writer = source.writeStream.format(dest.format).trigger(processingTime="10s")
        return writer.start()
