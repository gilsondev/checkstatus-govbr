import pandas as pd
from loguru import logger


def _normalize_text(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[f"{column}_normalized"] = (
        df[column]
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf8")
        .str.lower()
    )

    return df


def generate_slug_column(df: pd.DataFrame) -> pd.DataFrame:
    df["slug"] = df["domain"].str.split(pat=".gov.br").str[0]

    return df


def normalize_document_column(df: pd.DataFrame) -> pd.DataFrame:
    df["document_normalized"] = df["document"].replace(
        to_replace=r"\D", value="", regex=True
    )

    return df


def normalize_organization_column(df: pd.DataFrame) -> pd.DataFrame:
    return _normalize_text(df, "organization")


def normalize_agent_column(df: pd.DataFrame) -> pd.DataFrame:
    return _normalize_text(df, "agent")


# TODO: Need test
def normalize_department_column(df: pd.DataFrame) -> pd.DataFrame:
    if "department" in df.columns:
        df = _normalize_text(df, "department")
    return df


def normalize_timestamp_to_datetime(df: pd.DataFrame) -> pd.DataFrame:
    df["registered_at"] = pd.to_datetime(df["registered_at"])
    df["refreshed_at"] = pd.to_datetime(df["refreshed_at"])

    return df


def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Normalizing data")

    df = df.pipe(generate_slug_column)
    df = df.pipe(normalize_document_column)
    df = df.pipe(normalize_organization_column)
    df = df.pipe(normalize_department_column)
    df = df.pipe(normalize_agent_column)
    df = df.pipe(normalize_timestamp_to_datetime)

    logger.info("Data normalized")

    return df
