import sentry_sdk
from collect_csv import prepare_dataset
from collect_rdap import collect_domain_rdap_data
from ingestion import ingestion_data
from normalize import normalize_data
from sentry_sdk import set_tag

from lib.database import create_connection
from lib.database import create_cursor

sentry_sdk.init(
    dsn="https://011f53de8eea0a53cb44e163d0453eb5@o4506032925900800.ingest.sentry.io/4506032926031872",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)
set_tag("app", "Checkstatus Pipeline")

if __name__ == "__main__":
    conn = create_connection()
    cursor = create_cursor(conn)

    df = prepare_dataset()
    df = collect_domain_rdap_data(df)
    df = normalize_data(df)  # type: ignore

    ingestion_data(df, cursor)

    conn.commit()
    conn.close()
    cursor.close()
