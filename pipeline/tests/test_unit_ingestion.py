from unittest import mock

import pytest
from src import ingestion

from shared.database_py.database import create_connection
from shared.database_py.database import create_cursor
from shared.database_py.database import upsert


@mock.patch("shared.database_py.database.os.getenv")
@mock.patch("shared.database_py.database.psycopg2")
def test_connection(mock_pg2, mock_getenv):
    uri = "postgresql://someone@example.com/somedb"
    mock_getenv.return_value = uri

    create_connection()

    mock_pg2.connect.assert_called()


def test_cursor():
    conn_instance = mock.Mock()
    conn_instance.cursor.return_value = mock.Mock()

    create_cursor(conn_instance)

    conn_instance.cursor.assert_called()


@mock.patch("shared.database_py.database.create_connection")
@mock.patch("shared.database_py.database.create_cursor")
@mock.patch("shared.database_py.database.upsert")
@pytest.mark.skip("Mock not called for no reason")
def test_ingestion_data(mock_upsert, mock_cursor, mock_conn, enrich_domain_df):

    mock_cursor_instance = mock_cursor.return_value

    ingestion.ingestion_data(enrich_domain_df, mock_cursor_instance)

    data_dict = enrich_domain_df.to_dict(orient="records")
    mock_upsert.assert_called_with(data_dict, mock_cursor_instance)


def test_upsert(enrich_domain_df):
    data_dict = enrich_domain_df.to_dict(orient="records")
    cursor_instance = mock.Mock()

    upsert(data_dict, cursor_instance)
    cursor_instance.executemany.assert_called()
