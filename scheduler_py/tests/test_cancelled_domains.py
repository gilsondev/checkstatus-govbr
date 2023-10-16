from unittest.mock import MagicMock
from unittest.mock import patch

from src.cancelled_domains import CANCELLED_DOMAINS_CSV
from src.cancelled_domains import get_cancelled_domains
from src.cancelled_domains import update_domains


@patch("src.cancelled_domains.get_cancelled_domains")
@patch("src.cancelled_domains.update_domain_status")
def test_update_domains(mock_update_domain_status, mock_get_cancelled_domains):
    mock_df = MagicMock()
    mock_get_cancelled_domains.return_value = mock_df
    mock_cursor = MagicMock()

    update_domains(mock_cursor)

    mock_get_cancelled_domains.assert_called()
    mock_update_domain_status.assert_called_with(
        mock_df.to_dict(orient="records"), mock_cursor
    )


def test_get_cancelled_domains():
    # Create a mock logger
    mock_logger = MagicMock()

    # Patch the logger and the pd.read_csv function
    with patch("src.cancelled_domains.logger", mock_logger), patch(
        "src.cancelled_domains.pd.read_csv"
    ) as mock_read_csv:

        # Call the function
        get_cancelled_domains()

        # Assert that the logger was called with the correct message
        mock_logger.info.assert_called_once_with("Getting cancelled domains...")

        # Assert that pd.read_csv was called with the correct arguments
        mock_read_csv.assert_called_once_with(CANCELLED_DOMAINS_CSV, names=["domain"])
