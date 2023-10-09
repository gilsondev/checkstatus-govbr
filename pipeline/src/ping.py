import pandas as pd
import requests
from loguru import logger
from psycopg2.extensions import cursor
from requests import exceptions

from lib.database import insert_domain_availability


def check_availability(domain: str) -> bool:
    logger.info("Checking domain availability...")
    try:
        response = requests.head(f"http://{domain}", timeout=5)
        return response.status_code >= 200 and response.status_code < 400
    except (exceptions.ConnectionError, exceptions.Timeout):
        return False


def ping_domains(df: pd.DataFrame, cursor: cursor) -> bool:
    dataset = df.to_dict(orient="records")

    for data in dataset:
        result = check_availability(data["domain"])
        logger.info(f"Availability of Domain {data['domain']}: {result}")

        insert_domain_availability(data["domain"], result, cursor)
