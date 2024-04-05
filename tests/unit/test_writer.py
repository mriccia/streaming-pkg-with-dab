from streaming_pkg_with_dab.tasks.writer import Writer


def test_writer(kafka: str):
    w = Writer()
    w.get_bootstrap_server = lambda: kafka
    w.launch()
