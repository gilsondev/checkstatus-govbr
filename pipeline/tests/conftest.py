from pathlib import Path

import pandas as pd
import pytest


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
