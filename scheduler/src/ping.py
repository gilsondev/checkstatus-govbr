import requests
from loguru import logger
from psycopg2.extensions import cursor
from requests import exceptions

from lib.database import fetch_domains
from lib.database import insert_domain_availability


def check_availability(domain: str) -> bool:
    logger.info("Checking domain availability...")
    try:
        response = requests.head(f"http://{domain}", timeout=5)
        return response.status_code >= 200 and response.status_code < 400
    except (exceptions.ConnectionError, exceptions.Timeout):
        return False


def ping_domains(cursor: cursor) -> bool:
    dataset = fetch_domains(["domain", "available"])
    domains_status = []

    for data in dataset:
        result = check_availability(data.domain)
        logger.info(f"Availability of Domain {data.domain}: {result}")
        domains_status.append({"domain": data.domain, "available": result})

    logger.info(f"Inserting {len(domains_status)} domains status")
    insert_domain_availability(domains_status, cursor)
