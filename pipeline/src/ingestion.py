import os
from typing import List

import pandas as pd
import psycopg2

CONN_VARIABLES = {
    "host": os.getenv("DATABASE_HOST", "localhost"),
    "port": os.getenv("DATABASE_PORT", 5432),
    "database": os.getenv("DATABASE_NAME", "checkstatusgovbr"),
    "user": os.getenv("DATABASE_USER", "checkstatus"),
    "password": os.getenv("DATABASE_PASS", "passw0rd"),
}


def create_connection(
    host: str, port: int, database: str, user: str, password: str
) -> psycopg2.extensions.connection:
    return psycopg2.connect(
        host=host, port=port, database=database, user=user, password=password
    )  # noqa


def create_cursor(conn: psycopg2.extensions.connection) -> psycopg2.extensions.cursor:
    return conn.cursor()


def upsert(data: List[dict], cursor: psycopg2.extensions.cursor) -> None:
    query = """
    INSERT INTO domains (
        domain,
        slug,
        document,
        organization,
        agent,
        registered_at,
        refreshed_at,
        created_at
    )
    VALUES (
        %(domain)s, %(slug)s, %(document)s, %(organization)s,
        %(agent)s, %(registered_at)s, %(refreshed_at)s, NOW()
    )
    ON CONFLICT (domain)
    DO UPDATE SET
        document = EXCLUDED.document,
        organization = EXCLUDED.organization,
        agent = EXCLUDED.agent,
        refreshed_at = EXCLUDED.refreshed_at,
        updated_at = NOW()
    """

    cursor.executemany(query, data)


def ingestion_data(df: pd.DataFrame) -> None:
    conn = create_connection(**CONN_VARIABLES)
    cursor = create_cursor(conn)

    upsert(df.to_dict(orient="records"), cursor)  # type: ignore
    conn.commit()
    conn.close()
    cursor.close()
