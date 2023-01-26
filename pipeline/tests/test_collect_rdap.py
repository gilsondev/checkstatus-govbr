from unittest import mock

from src.collect_rdap import RDAPDomain


def _prepare_mock(mock_whoisit, rdap_response_json):
    mock_whoisit.is_bootstrapped.return_value = True
    mock_whoisit.domain.return_value = rdap_response_json

    with mock.patch("src.utils.sleep"):
        rdap = RDAPDomain(domain="gdf.gov.br")
        rdap._fetch_data()
        return rdap


@mock.patch("src.collect_rdap.whoisit")
def test_fetch_rdap_domain(mock_whoisit, rdap_response_json):
    rdap = _prepare_mock(mock_whoisit, rdap_response_json)
    assert "handle" in rdap.data.keys()


@mock.patch("src.collect_rdap.whoisit")
def test_rdap_nameservers(mock_whoisit, rdap_response_json):
    rdap = _prepare_mock(mock_whoisit, rdap_response_json)
    assert ["dns1.gdfnet.df.gov.br", "dns2.df.gov.br"] == rdap.nameservers


@mock.patch("src.collect_rdap.whoisit")
def test_rdap_department(mock_whoisit, rdap_response_json):
    rdap = _prepare_mock(mock_whoisit, rdap_response_json)

    assert {
        "name": "Suporte Técnico - CODEPLAN",
        "email": "suporte@gdfnet.df.gov.br",
    } == rdap.department


@mock.patch("src.collect_rdap.whoisit")
def test_rdap_status(mock_whoisit, rdap_response_json):
    rdap = _prepare_mock(mock_whoisit, rdap_response_json)

    assert rdap.domain_status == ["active"]
