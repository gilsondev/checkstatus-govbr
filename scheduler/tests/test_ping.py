from unittest.mock import MagicMock
from unittest.mock import patch

from src.ping import ping_domains


@patch("src.ping.fetch_domains")
@patch("src.ping.check_availability")
@patch("src.ping.insert_domain_availability")
def test_ping_domains(
    mock_insert_domain_availability,
    mock_check_availability,
    mock_fetch_domains,
):
    # Mocking the fetch_domains function to return a list of domains
    mock_fetch_domains.return_value = [
        MagicMock(domain="example.com"),
        MagicMock(domain="example.org"),
    ]

    mock_check_availability.side_effect = [True, False]

    # Calling the function to be tested
    ping_domains(MagicMock())

    mock_check_availability.assert_any_call("example.com")
    mock_check_availability.assert_any_call("example.org")

    mock_insert_domain_availability.assert_called()
