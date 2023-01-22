import time
import pytest
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
class TestWeb:
    def test_verify_login(self):
        WebFlows.login_flow('admin', 'admin')
        WebFlows.verify_grafana_title("Welcome to Grafana")
