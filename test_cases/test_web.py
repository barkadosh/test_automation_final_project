import time
import pytest


@pytest.mark.usefixtures('init_web_driver')
class TestWeb:
    def test_kuku(self):
        time.sleep(1)

