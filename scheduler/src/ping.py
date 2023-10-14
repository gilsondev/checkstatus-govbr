import concurrent
from concurrent.futures import ThreadPoolExecutor

import requests
from loguru import logger
from psycopg2.extensions import cursor
from requests import exceptions

from lib.database import fetch_domains
from lib.database import insert_domain_availability


def check_availability(domain: str) -> bool:
    logger.info("Checking domain availability...")
    try:
        response = requests.head(f"http://{domain}", timeout=30, verify=False)
        return response.status_code >= 200 and response.status_code < 500
    except (exceptions.ConnectionError, exceptions.Timeout):
        return False


def ping_domains(cursor: cursor):
    dataset = fetch_domains(["domain", "available"])
    domains_status = []

    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(check_availability, data.domain): data
            for data in dataset  # noqa
        }

        for future in concurrent.futures.as_completed(futures):
            data = futures[future]
            try:
                result = future.result()
                logger.info(f"Availability of Domain {data.domain}: {result}")
                domains_status.append(
                    {"domain": data.domain, "available": result}
                )  # noqa
            except Exception as e:
                logger.error(f"Error checking domain {data.domain}: {e}")

    if len(domains_status) > 0:
        logger.info(f"Inserting {len(domains_status)} domains status")
        insert_domain_availability(domains_status, cursor)
