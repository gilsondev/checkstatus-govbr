from unittest import mock

from src.collect_rdap import insert_rdap_dataframe
from src.collect_rdap import RDAPDomain


def _prepare_mock(rdap_response_json):
    with mock.patch("collect_rdap.whoisit") as mock_whoisit:
        mock_whoisit.is_bootstrapped.return_value = True
        mock_whoisit.domain.return_value = rdap_response_json

        with mock.patch("utils.sleep"):
            rdap = RDAPDomain(domain="gdf.gov.br")
            rdap._fetch_data()
            return rdap


def test_fetch_rdap_domain(rdap_response_json):
    rdap = _prepare_mock(rdap_response_json)
    assert "handle" in rdap.data.keys()


def test_rdap_nameservers(rdap_response_json):
    rdap = _prepare_mock(rdap_response_json)
    assert ["dns1.gdfnet.df.gov.br", "dns2.df.gov.br"] == rdap.nameservers


def test_rdap_department(rdap_response_json):
    rdap = _prepare_mock(rdap_response_json)

    assert {
        "name": "Suporte Técnico - CODEPLAN",
        "email": "suporte@gdfnet.df.gov.br",
    } == rdap.department


def test_rdap_status(rdap_response_json):
    rdap = _prepare_mock(rdap_response_json)

    assert rdap.domain_status == ["active"]


def test_insert_rdap_dataframe(raw_domain_df):
    with mock.patch("src.collect_rdap.whoisit"):
        with mock.patch("src.utils.sleep"):
            result_df = insert_rdap_dataframe(raw_domain_df)
            assert "nameservers" in result_df.columns.tolist()
            assert "department" in result_df.columns.tolist()
            assert "department_email" in result_df.columns.tolist()
            assert "status" in result_df.columns.tolist()
