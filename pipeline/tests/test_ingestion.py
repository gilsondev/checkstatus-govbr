from datetime import datetime

from lib.database import upsert


def test_upsert(connection, cursor, enrich_domain_df):
    data_dict = enrich_domain_df.to_dict(orient="records")
    upsert(data_dict, cursor)
    connection.commit()

    cursor.execute("SELECT * FROM domains")
    result = cursor.fetchone()

    registered_at = datetime.strptime(data_dict[0]["registered_at"], "%m/%d/%y %H:%M")
    refreshed_at = datetime.strptime(data_dict[0]["refreshed_at"], "%m/%d/%y %H:%M")

    assert result is not None
    assert result["domain"] == data_dict[0]["domain"]
    assert result["document"] == data_dict[0]["document"]
    assert result["document_normalized"] == data_dict[0]["document_normalized"]
    assert result["organization"] == data_dict[0]["organization"]
    assert result["organization_normalized"] == data_dict[0]["organization_normalized"]
    assert result["agent"] == data_dict[0]["agent"]
    assert result["agent_normalized"] == data_dict[0]["agent_normalized"]
    assert result["nameservers"] == data_dict[0]["nameservers"]
    assert result["department"] == data_dict[0]["department"]
    assert result["department_normalized"] == data_dict[0]["department_normalized"]
    assert result["department_email"] == data_dict[0]["department_email"]
    assert result["status"] == data_dict[0]["status"]
    assert result["registered_at"] == registered_at
    assert result["refreshed_at"] == refreshed_at
