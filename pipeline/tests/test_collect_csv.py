from pathlib import Path
from unittest import mock

from src.collect_csv import prepare_dataset

SAMPLE_CSV = Path(__file__).parent.parent / "src/sample_data/domains.csv"


@mock.patch("src.collect_csv.DOMAIN_DATASET_CSV", str(SAMPLE_CSV))
def test_collect_csv():
    df = prepare_dataset()

    print(df.columns)
    assert df is not None
    columns = df.columns.tolist()

    assert columns == [
        "domain",
        "organization",
        "document",
        "agent",
        "registered_at",
        "refreshed_at",
    ]
