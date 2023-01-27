from src.ingestion import upsert


def test_upsert(connection, cursor, enrich_domain_df):
    data_dict = enrich_domain_df.to_dict(orient="records")
    upsert(data_dict, cursor)
    connection.commit()

    cursor.execute("SELECT COUNT(*) FROM domains")
    result = cursor.fetchone()

    assert result[0] == 1
