from unittest import mock

from src.collect_rdap import insert_rdap_dataframe
from src.collect_rdap import RDAPDomain


def _prepare_mock(rdap_response_json):
    with mock.patch("src.collect_rdap.whoisit") as mock_whoisit:
        mock_whoisit.is_bootstrapped.return_value = True
        mock_whoisit.domain.return_value = rdap_response_json

        rdap = RDAPDomain()
        rdap.fetch_data("gdf.gov.br")
        return rdap


@mock.patch("src.collect_rdap.time.sleep")
def test_fetch_rdap_domain(mock_sleep, rdap_response_json):
    rdap = _prepare_mock(rdap_response_json)
    assert "handle" in rdap.data.keys()


@mock.patch("src.collect_rdap.time.sleep")
def test_rdap_nameservers(mock_sleep, rdap_response_json):
    rdap = _prepare_mock(rdap_response_json)
    assert ["dns1.gdfnet.df.gov.br", "dns2.df.gov.br"] == rdap.nameservers


@mock.patch("src.collect_rdap.time.sleep")
def test_rdap_department(mock_sleep, rdap_response_json):
    rdap = _prepare_mock(rdap_response_json)

    assert {
        "name": "Suporte Técnico - CODEPLAN",
        "email": "suporte@gdfnet.df.gov.br",
    } == rdap.department


@mock.patch("src.collect_rdap.time.sleep")
def test_rdap_status(mock_sleep, rdap_response_json):
    rdap = _prepare_mock(rdap_response_json)

    assert rdap.domain_status == ["active"]


@mock.patch("src.collect_rdap.whoisit")
@mock.patch("src.collect_rdap.time.sleep")
def test_insert_rdap_dataframe(mock_sleep, mock_whoisit, raw_domain_df):
    mock_whoisit.is_bootstrapped.return_value = True
    mock_whoisit.domain.return_value = {
        "status": ["active"],
        "entities": {
            "technical": [{"name": "Example", "email": "admin@example.com"}]
        },  # noqa
        "nameservers": ["ns1.example.com"],
        "department": {
            "name": "Example Department",
            "email": "admin@example.com",
        },  # noqa
    }

    result_df = insert_rdap_dataframe(raw_domain_df)
    assert "nameservers" in result_df.columns.tolist()
    assert "department" in result_df.columns.tolist()
    assert "department_email" in result_df.columns.tolist()
    assert "status" in result_df.columns.tolist()
