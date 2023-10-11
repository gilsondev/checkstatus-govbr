import os
from collections import namedtuple
from typing import List

import psycopg2
from psycopg2.extensions import connection
from psycopg2.extensions import cursor
from psycopg2.extensions import parse_dsn
from psycopg2.extras import execute_batch


def create_connection() -> connection:
    database_url = os.getenv("DATABASE_URL")
    dsn = parse_dsn(database_url)
    return psycopg2.connect(**dsn)  # noqa


def create_cursor(conn: connection) -> cursor:
    return conn.cursor()


def fetch_domains(fields: List[str]) -> List[dict]:
    domain = namedtuple("Domain", fields)
    query = f"""
    SELECT {",".join(fields)} FROM domains WHERE NOT 'canceled' = ANY(status);
    """
    cursor = create_cursor(create_connection())
    cursor.execute(query)

    result = cursor.fetchall()
    return [domain(*row) for row in result]


def upsert(data: List[dict], cursor: cursor) -> None:
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


def update(dataset: List[dict], fields: List[str], cursor) -> None:
    fields_to_update = ", ".join([f"{field} = %({field})s" for field in fields if field != "domain"])

    query = f"UPDATE domains SET {fields_to_update} WHERE domain = %(domain)s"

    execute_batch(cursor, query, dataset)


def insert_domain_availability(dataset: List[dict], cursor: cursor) -> None:
    update(dataset, ["available"], cursor)


def update_domain_status(dataset: List[dict], cursor: cursor) -> None:
    query = "UPDATE domains SET status = ARRAY['canceled'], available = false WHERE domain = %(domain)s"  # noqa

    execute_batch(cursor, query, dataset)
