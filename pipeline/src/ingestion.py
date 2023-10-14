import pandas as pd
from psycopg2.extensions import cursor

from lib.python.database import upsert


def ingestion_data(df: pd.DataFrame, cursor: cursor) -> None:
    upsert(df.to_dict(orient="records"), cursor)  # type: ignore
