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
    SELECT {",".join(fields)} FROM domains;
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
        available,
        registered_at,
        refreshed_at,
        created_at
    )
    VALUES (
        %(domain)s, %(slug)s, %(document)s, %(document_normalized)s,
        %(organization)s, %(organization_normalized)s, %(agent)s,
        %(agent_normalized)s, %(nameservers)s, %(department)s,
        %(department_normalized)s, %(department_email)s, %(status)s,
        false, %(registered_at)s, %(refreshed_at)s, NOW()
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
        available = EXCLUDED.available,
        refreshed_at = EXCLUDED.refreshed_at,
        updated_at = NOW()
    """

    cursor.executemany(query, data)


def insert_domain_availability(
    domain: str, available: bool, cursor: cursor
) -> None:  # noqa
    query = """
    UPDATE domains SET available = %(available)s WHERE domain = %(domain)s
    """

    cursor.execute(query, {"domain": domain, "available": available})


def insert_domain_availability(dataset: List[dict], cursor: cursor) -> None:  # noqa
    query = """
    UPDATE domains SET available = %(available)s WHERE domain = %(domain)s
    """

    execute_batch(cursor, query, dataset)
