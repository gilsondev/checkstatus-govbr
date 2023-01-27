import os
from typing import List

import pandas as pd
import psycopg2
from psycopg2.extensions import parse_dsn


def create_connection(uri: str) -> psycopg2.extensions.connection:
    dsn = parse_dsn(uri)
    return psycopg2.connect(**dsn)  # noqa


def create_cursor(conn: psycopg2.extensions.connection) -> psycopg2.extensions.cursor:
    return conn.cursor()


def upsert(data: List[dict], cursor: psycopg2.extensions.cursor) -> None:
    query = """
    INSERT INTO domains (
        domain,
        slug,
        document,
        document_normalized,
        organization,
        organization_normalized,
        agent,
        agent_normalized,
        nameservers,
        department,
        department_normalized,
        department_email,
        status,
        registered_at,
        refreshed_at,
        created_at
    )
    VALUES (
        %(domain)s, %(slug)s, %(document)s, %(document_normalized)s,
        %(organization)s, %(organization_normalized)s, %(agent)s,
        %(agent_normalized)s, %(nameservers)s, %(department)s,
        %(department_normalized)s, %(department_email)s, %(status)s,
        %(registered_at)s, %(refreshed_at)s, NOW()
    )
    ON CONFLICT (domain)
    DO UPDATE SET
        document = EXCLUDED.document,
        document_normalized = EXCLUDED.document_normalized,
        organization = EXCLUDED.organization,
        organization_normalized = EXCLUDED.organization_normalized,
        agent = EXCLUDED.agent,
        agent_normalized = EXCLUDED.agent_normalized,
        nameservers = EXCLUDED.nameservers,
        department = EXCLUDED.department,
        department_normalized = EXCLUDED.department_normalized,
        status = EXCLUDED.status,
        refreshed_at = EXCLUDED.refreshed_at,
        updated_at = NOW()
    """

    cursor.executemany(query, data)


def ingestion_data(df: pd.DataFrame) -> None:
    database_url = os.getenv("DATABASE_URL")
    conn = create_connection(database_url)
    cursor = create_cursor(conn)

    upsert(df.to_dict(orient="records"), cursor)  # type: ignore
    conn.commit()
    conn.close()
    cursor.close()
