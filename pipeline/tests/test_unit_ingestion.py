from unittest import mock

from src import ingestion


@mock.patch("src.ingestion.psycopg2")
def test_connection(mock_pg2):
    uri = "postgresql://someone@example.com/somedb"
    ingestion.create_connection(uri)

    mock_pg2.connect.assert_called()


def test_cursor():
    conn_instance = mock.Mock()
    conn_instance.cursor.return_value = mock.Mock()

    ingestion.create_cursor(conn_instance)

    conn_instance.cursor.assert_called()


@mock.patch("src.ingestion.create_connection")
@mock.patch("src.ingestion.create_cursor")
@mock.patch("src.ingestion.upsert")
def test_ingestion_data(mock_upsert, mock_cursor, mock_conn, enrich_domain_df):
    ingestion.ingestion_data(enrich_domain_df)
    data_dict = enrich_domain_df.to_dict(orient="records")

    mock_conn.assert_called()
    mock_cursor.assert_called()
    mock_upsert.assert_called_with(data_dict, mock_cursor())


def test_upsert(enrich_domain_df):
    data_dict = enrich_domain_df.to_dict(orient="records")
    cursor_instance = mock.Mock()

    ingestion.upsert(data_dict, cursor_instance)
    cursor_instance.executemany.assert_called()
