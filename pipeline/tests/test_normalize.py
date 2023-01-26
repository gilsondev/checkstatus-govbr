import numpy as np
from src import normalize


def test_generate_slug_column(raw_domain_df):
    result_df = raw_domain_df.pipe(normalize.generate_slug_column)
    schema_new_columns = result_df.dtypes.to_dict()
    fieldname = "slug"

    assert fieldname in schema_new_columns.keys()
    assert np.dtype(object) == schema_new_columns.get(fieldname)
    assert "abin" == result_df[fieldname][0]


def test_normalize_document_column(raw_domain_df):
    result_df = raw_domain_df.pipe(normalize.normalize_document_column)
    schema_new_columns = result_df.dtypes.to_dict()
    fieldname = "document_normalized"

    assert fieldname in schema_new_columns.keys()
    assert np.dtype(object) == schema_new_columns.get(fieldname)
    assert "001175497000141" == result_df[fieldname][0]


def test_normalize_organization_column(raw_domain_df):
    result_df = raw_domain_df.pipe(normalize.normalize_organization_column)
    schema_new_columns = result_df.dtypes.to_dict()
    fieldname = "organization_normalized"

    assert fieldname in schema_new_columns.keys()
    assert np.dtype(object) == schema_new_columns.get(fieldname)
    assert "agencia brasileira de inteligencia" == result_df[fieldname][0]


def test_normalize_timestamp_to_datetime(raw_domain_df):
    result_df = raw_domain_df.pipe(normalize.normalize_timestamp_to_datetime)
    schema_new_columns = result_df.dtypes.to_dict()

    field_registered, field_refreshed = "registered_at", "refreshed_at"

    assert np.dtype("datetime64[ns]") == schema_new_columns.get(field_registered)
    assert np.dtype("datetime64[ns]") == schema_new_columns.get(field_refreshed)


def test_normalize_agent_column(raw_domain_df):
    result_df = raw_domain_df.pipe(normalize.normalize_agent_column)
    schema_new_columns = result_df.dtypes.to_dict()
    fieldname = "agent_normalized"

    assert fieldname in schema_new_columns.keys()
    assert np.dtype(object) == schema_new_columns.get(fieldname)
    assert "rodrigo bastos vasconcelos teperino" == result_df[fieldname][0]


def test_normalize_data(raw_domain_df):
    result_df = normalize.normalize_data(raw_domain_df)
    columns = result_df.columns.tolist()

    assert "slug" in columns
    assert "document_normalized" in columns
    assert "organization_normalized" in columns
