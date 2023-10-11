import concurrent.futures
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
        time.sleep(random.randint(1, 5))  # sleep aleatório de 1 a 5 segundos

        logger.info(f"Fetching RDAP data from domain {domain}.")
        self.data = whoisit.domain(domain)

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


def insert_rdap_dataframe(row: dict) -> dict:
    rdap = RDAPDomain()
    rdap.fetch_data(row["domain"])
    row["nameservers"] = rdap.nameservers

    department = rdap.department
    row["department"] = department.get("name")
    row["department_email"] = department.get("email")
    row["status"] = rdap.domain_status

    return row


def collect_domain_rdap_data(df: pd.DataFrame) -> pd.DataFrame:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(insert_rdap_dataframe, df.to_dict("records"))

    return pd.DataFrame(results)
