import requests
from loguru import logger
from requests import exceptions


def check_availability(domain: str) -> bool:
    logger.info("Checking domain availability...")
    try:
        response = requests.head(f"http://{domain}", timeout=5)
        return response.status_code >= 200 and response.status_code < 400
    except (exceptions.ConnectionError, exceptions.Timeout):
        return False
