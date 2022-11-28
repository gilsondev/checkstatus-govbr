import pandas as pd
from loguru import logger


def _normalize_text(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[f"{column}_normalized"] = (
        df[column]
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8")
        .str.lower()
    )
    df[f"{column}_normalized"] = df[f"{column}_normalized"].replace(
        to_replace=r"[0-9.\-]", value="", regex=True
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


def prepare_dataset(csv_url_path: str) -> pd.DataFrame:
    df = pd.read_csv(
        csv_url_path,
        names=[
            "domain",
            "document",
            "organization",
            "agent",
            "registered_at",
            "refreshed_at",
        ],
        skiprows=1,
        parse_dates=["registered_at", "refreshed_at"],
    )
    return df


def normalize_data(csv_url_path: str) -> pd.DataFrame:
    logger.info("Downloading CSV dataset...")

    df = prepare_dataset(csv_url_path)

    logger.info("Normalizing data")
    df = df.pipe(generate_slug_column)
    df = df.pipe(normalize_document_column)
    df = df.pipe(normalize_organization_column)
    df = df.pipe(normalize_agent_column)

    logger.info("Data normalized")

    return df
