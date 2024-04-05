from typing import Generator

import pytest
from testcontainers.kafka import KafkaContainer

from streaming_pkg_with_dab.config import DefaultConfig


@pytest.fixture(scope="session")
def kafka() -> Generator[str, None, None]:
    with KafkaContainer() as _kafka:
        connection = _kafka.get_bootstrap_server()
        yield connection


@pytest.fixture(scope="session")
def cfg(kafka) -> DefaultConfig:
    return DefaultConfig(kafka={"bootstrap_servers": kafka})
