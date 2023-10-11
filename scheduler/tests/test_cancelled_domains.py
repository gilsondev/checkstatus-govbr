from unittest.mock import MagicMock
from unittest.mock import patch

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
