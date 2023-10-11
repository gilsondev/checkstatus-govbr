import os

import pandas as pd
from loguru import logger
from psycopg2.extensions import cursor

from lib.database import update_domain_status

CANCELLED_DOMAINS_CSV = os.getenv(
    "CANCELLED_DOMAINS_CSV",
    "https://www.gov.br/governodigital/pt-br/transformacao-digital/ferramentas/unificacao-de-canais/lista-de-dominios-cancelados.csv",  # noqa
)


def get_cancelled_domains() -> pd.DataFrame:
    logger.info("Getting cancelled domains...")
    return pd.read_csv(CANCELLED_DOMAINS_CSV, names=["domain"])


def update_domains(cursor: cursor) -> None:
    logger.info("Updating cancelled domains...")
    df = get_cancelled_domains()

    update_domain_status(df.to_dict(orient="records"), cursor)
