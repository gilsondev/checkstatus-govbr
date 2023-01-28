from typing import List

import pandas as pd
import whoisit
from loguru import logger
from tenacity import retry
from tenacity import stop
from utils import delay_call


class RDAPDomain:
    def __init__(self, domain: str) -> None:
        self.domain = domain
        self.data = dict()

        if not whoisit.is_bootstrapped():
            whoisit.bootstrap()
        self._fetch_data()

    @retry(stop=stop.stop_after_attempt(7))
    @delay_call(min=2, max=10)
    def _fetch_data(self) -> None:
        logger.info(f"Fetching RDAP data from domain {self.domain}.")
        self.data = whoisit.domain(self.domain)

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
    rdap = RDAPDomain(domain=df["domain"])
    df["nameservers"] = rdap.nameservers
    df["department"] = rdap.department.get("name")
    df["department_email"] = rdap.department.get("email")
    df["status"] = rdap.domain_status

    return df


def collect_domain_rdap_data(df: pd.DataFrame) -> pd.DataFrame | pd.Series:
    return df.apply(insert_rdap_dataframe, axis=1)
