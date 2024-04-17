import shutil
import tempfile
from pathlib import Path
from typing import Generator

import pytest
from delta import configure_spark_with_delta_pip
from dotenv import load_dotenv
from loguru import logger
from pyspark.sql import SparkSession
from testcontainers.kafka import KafkaContainer

from streaming_pkg_with_dab.config import DefaultConfig, KafkaInfo, ReaderInfo


@pytest.fixture(scope="session", autouse=True)
def env():
    _env = Path(".env")
    if _env.exists():
        load_dotenv(_env)
    else:
        logger.warning("No .env file found")


@pytest.fixture(scope="session", autouse=True)
def spark():
    """
    This fixture provides preconfigured SparkSession with Hive and Delta support.
    After the test session, temporary warehouse directory is deleted.
    :return: SparkSession
    """
    logger.debug("Configuring Spark session for testing environment")
    warehouse_dir = tempfile.TemporaryDirectory().name
    _builder = (
        SparkSession.builder.master("local[1]")
        .config("spark.hive.metastore.warehouse.dir", Path(warehouse_dir).as_uri())
        .config("spark.default.parallelism", 4)  # purely for testing purposes!
        .config("spark.sql.shuffle.partitions", 4)  # purely for testing purposes!
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    )
    _builder = configure_spark_with_delta_pip(
        _builder, extra_packages=["org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"]
    )
    spark: SparkSession = _builder.getOrCreate()
    logger.info("Spark session configured")
    yield spark
    logger.info("Shutting down Spark session")
    spark.stop()
    if Path(warehouse_dir).exists():
        shutil.rmtree(warehouse_dir)


@pytest.fixture(scope="session")
def checkpoint_dir() -> str:
    return tempfile.mkdtemp()


@pytest.fixture(scope="session")
def kafka() -> Generator[str, None, None]:
    with KafkaContainer() as _kafka:
        connection = _kafka.get_bootstrap_server()
        yield connection


@pytest.fixture(scope="session")
def cfg(kafka, checkpoint_dir: str) -> DefaultConfig:
    return DefaultConfig(
        kafka=KafkaInfo(bootstrap_servers=kafka, topic="test"), reader=ReaderInfo(checkpoint_location=checkpoint_dir)
    )
