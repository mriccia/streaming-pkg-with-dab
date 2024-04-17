from kafka import KafkaProducer
from pyspark.sql import SparkSession

from streaming_pkg_with_dab.config import DefaultConfig
from streaming_pkg_with_dab.tasks.reader import Reader


def test_reader(cfg: DefaultConfig, spark: SparkSession):
    prod = KafkaProducer(bootstrap_servers=cfg.kafka.bootstrap_servers, acks="all")
    for _ in range(10):
        prod.send(cfg.kafka.topic, b"test")
    prod.flush()
    prod.close()
    r = Reader(cfg)
    r.launch()
    assert spark.table(cfg.reader.output_table).count() == 10
