import time
import pytest
from utilities.common_ops import get_data
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
class TestWeb:
    def test_verify_login(self):
        WebFlows.login_flow(get_data('Username'), get_data('Password'))
        WebFlows.verify_grafana_title("Welcome to Grafana")
