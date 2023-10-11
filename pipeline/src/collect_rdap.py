import random
import time
from typing import List

import pandas as pd
import whoisit
from loguru import logger


class RDAPDomain:
    def __init__(self) -> None:
        self.data = dict()

        if not whoisit.is_bootstrapped():
            whoisit.bootstrap()

    def fetch_data(self, domain: str) -> None:
        try:
            time.sleep(random.randint(3, 15))  # sleep aleatório de 3 a 15 segundos
            logger.info(f"Fetching RDAP data from domain {domain}.")

            self.data = whoisit.domain(domain)
            logger.info(f"RDAP data fetched for domain {domain}.")
        except whoisit.errors.QueryError as e:
            logger.error(f"Error fetching RDAP data for domain {domain}: {e}")

    @property
    def nameservers(self) -> List[str]:
        return self.data.get("nameservers", [])

    @property
    def department(self) -> dict:
        department = {}
        department_data = self.data.get("entities", {}).get("technical", [])
        if len(department_data) > 0:
            department_data = department_data[0]
            department = {
                "name": department_data.get("name"),
                "email": department_data.get("email"),
            }

        return department

    @property
    def domain_status(self):
        return self.data.get("status", [])


def insert_rdap_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    rdap = RDAPDomain()
    rdap.fetch_data(df["domain"])
    df["nameservers"] = rdap.nameservers
    df["department"] = rdap.department.get("name")
    df["department_email"] = rdap.department.get("email")
    df["status"] = rdap.domain_status

    return df


def collect_domain_rdap_data(df: pd.DataFrame) -> pd.DataFrame | pd.Series:
    return df.apply(insert_rdap_dataframe, axis=1)
