import os

import pandas as pd
from loguru import logger

DOMAIN_DATASET_CSV = os.getenv(
    "DOMAIN_DATASET_CSV",
    "https://repositorio.dados.gov.br/sgd/dominios/Dominios_GovBR_basico.csv",
)


def prepare_dataset() -> pd.DataFrame:
    logger.info("Downloading CSV dataset...")

    df = pd.read_csv(
        DOMAIN_DATASET_CSV,
        names=[
            "domain",
            "organization",
            "document",
            "agent",
            "registered_at",
            "refreshed_at",
        ],
        delimiter=";",
        encoding="latin-1",
        skiprows=1,
        header=None,
        parse_dates=["registered_at", "refreshed_at"],
    )

    return df
