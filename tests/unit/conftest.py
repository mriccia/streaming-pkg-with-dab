import pytest
from testcontainers.kafka import KafkaContainer


@pytest.fixture(scope="session")
def kafka():
    with KafkaContainer() as _kafka:
        connection = _kafka.get_bootstrap_server()
        yield connection
