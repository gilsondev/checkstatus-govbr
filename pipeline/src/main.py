from collect_csv import prepare_dataset
from collect_rdap import collect_domain_rdap_data
from ingestion import ingestion_data
from normalize import normalize_data
from ping import ping_domains

from lib.database import create_connection
from lib.database import create_cursor

if __name__ == "__main__":
    conn = create_connection()
    cursor = create_cursor(conn)

    df = prepare_dataset()
    df = collect_domain_rdap_data(df)
    df = normalize_data(df)  # type: ignore

    ingestion_data(df, cursor)
    ping_domains(df, cursor)

    conn.commit()
    conn.close()
    cursor.close()
