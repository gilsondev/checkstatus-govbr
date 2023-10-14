from urllib.error import URLError

import pandas as pd
from loguru import logger
from psycopg2.extensions import cursor
from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_fixed

from lib.python.database import update_domain_status

CANCELLED_DOMAINS_CSV = "https://www.gov.br/governodigital/pt-br/transformacao-digital/ferramentas/unificacao-de-canais/lista-de-dominios-cancelados.csv"  # noqa


@retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
def get_cancelled_domains() -> pd.DataFrame:
    logger.info("Getting cancelled domains...")
    try:
        return pd.read_csv(CANCELLED_DOMAINS_CSV, names=["domain"])
    except URLError as e:
        logger.warning(f"Error while fetching cancelled domains: {e}")
        raise ConnectionResetError("Connection reset by peer") from e


def update_domains(cursor: cursor) -> None:
    logger.info("Updating cancelled domains...")
    df = get_cancelled_domains()

    update_domain_status(df.to_dict(orient="records"), cursor)
