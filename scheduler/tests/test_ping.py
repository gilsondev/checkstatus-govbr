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


@patch("src.ping.fetch_domains")
@patch("src.ping.check_availability")
@patch("src.ping.insert_domain_availability")
def test_ping_domains_with_empty_dataset(
    mock_insert_domain_availability,
    mock_check_availability,
    mock_fetch_domains,
):
    # Mocking the fetch_domains function to return an empty list
    mock_fetch_domains.return_value = []

    # Calling the function to be tested
    ping_domains(MagicMock())

    mock_check_availability.assert_not_called()
    mock_insert_domain_availability.assert_not_called()


@patch("src.ping.fetch_domains")
@patch("src.ping.check_availability")
@patch("src.ping.insert_domain_availability")
def test_ping_domains_with_exception(
    mock_insert_domain_availability,
    mock_check_availability,
    mock_fetch_domains,
):
    # Mocking the fetch_domains function to return a list of domains
    mock_fetch_domains.return_value = [
        MagicMock(domain="example.com"),
        MagicMock(domain="example.org"),
    ]

    # Mocking the check_availability function to raise an exception
    mock_check_availability.side_effect = Exception("Something went wrong")

    # Calling the function to be tested
    ping_domains(MagicMock())

    # Asserting that the exception was caught and logged
    mock_insert_domain_availability.assert_not_called()
