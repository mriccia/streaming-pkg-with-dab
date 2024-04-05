from streaming_pkg_with_dab.config import DefaultConfig
from streaming_pkg_with_dab.tasks.writer import Writer


def test_writer(cfg: DefaultConfig):
    w = Writer(cfg)
    w.launch()
