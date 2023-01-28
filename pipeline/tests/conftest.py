import datetime
import os

import pandas as pd
import psycopg2
import pytest
from dateutil.tz import tzutc
from psycopg2.extensions import parse_dsn
from psycopg2.extras import RealDictCursor


@pytest.fixture(scope="session")
def connection():
    dsn = parse_dsn(
        os.getenv(
            "TEST_DATABASE_URL",
            "postgresql://postgres:postgres@localhost:5432/checkstatusgovbrtest",
        )
    )
    conn = psycopg2.connect(**dsn)  # noqa
    yield conn


@pytest.fixture(scope="session")
def cursor(connection):
    cur = connection.cursor(cursor_factory=RealDictCursor)
    yield cur
    cur.execute("TRUNCATE domains;")
    connection.commit()
    connection.close()


@pytest.fixture
def raw_domain_df():
    data = {
        "domain": ["abin.gov.br"],
        "document": ["001.175.497/0001-41"],
        "organization": ["Agencia Brasileira de Inteligencia"],
        "agent": ["Rodrigo Bastos Vasconcelos Teperino"],
        "registered_at": ["11/8/97 11:00"],
        "refreshed_at": ["6/1/20 17:12"],
    }
    yield pd.DataFrame(data=data)


@pytest.fixture
def rdap_response_json():
    data = {
        "handle": "GDF.GOV.BR",
        "parent_handle": "",
        "name": "gdf.gov.br",
        "whois_server": "whois.nic.br",
        "type": "domain",
        "terms_of_service_url": "",
        "copyright_notice": "",
        "description": [],
        "last_changed_date": datetime.datetime(2019, 9, 3, 15, 30, 18, tzinfo=tzutc()),
        "registration_date": datetime.datetime(1995, 4, 7, 12, 0, tzinfo=tzutc()),
        "expiration_date": None,
        "url": "https://rdap.registro.br/domain/gdf.gov.br",
        "rir": "registro.br",
        "entities": {
            "registrant": [
                {
                    "handle": "03230476000107",
                    "url": "https://rdap.registro.br/entity/03230476000107",
                    "type": "entity",
                    "name": "Sec. de Estado de Plan. e Orçamento do DF",
                    "rir": "registro.br",
                }
            ],
            "administrative": [
                {
                    "handle": "STC46",
                    "type": "entity",
                    "name": "Suporte Técnico - CODEPLAN",
                    "email": "suporte@gdfnet.df.gov.br",
                }
            ],
            "technical": [
                {
                    "handle": "STC46",
                    "type": "entity",
                    "name": "Suporte Técnico - CODEPLAN",
                    "email": "suporte@gdfnet.df.gov.br",
                }
            ],
        },
        "nameservers": ["dns1.gdfnet.df.gov.br", "dns2.df.gov.br"],
        "status": ["active"],
        "dnssec": False,
    }

    yield data


@pytest.fixture
def enrich_domain_df():
    data = {
        "domain": ["gdf.gov.br"],
        "slug": ["gdf"],
        "document": ["001.175.497/0001-41"],
        "document_normalized": ["001175497000141"],
        "organization": ["Agencia Brasileira de Inteligencia"],
        "organization_normalized": ["agencia brasileira de inteligencia"],
        "agent": ["Rodrigo Bastos Vasconcelos Teperino"],
        "agent_normalized": ["rodrigo bastos vasconcelos teperino"],
        "nameservers": [["dns1.gdfnet.df.gov.br", "dns2.df.gov.br"]],
        "department": ["Suporte Técnico - CODEPLAN"],
        "department_normalized": ["suporte tecnico - codeplan"],
        "department_email": "suporte@gdfnet.df.gov.br",
        "status": [["active"]],
        "registered_at": ["11/8/97 11:00"],
        "refreshed_at": ["6/1/20 17:12"],
    }
    yield pd.DataFrame(data=data)
