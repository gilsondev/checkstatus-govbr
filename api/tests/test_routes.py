import json

from freezegun import freeze_time
from src import __version__
from src.core.config import settings


def test_root_endpoint(client):
    resp = client.get("/")

    assert resp.status_code == 200
    assert resp.json() == {"app": settings.TITLE, "version": __version__}


@freeze_time("2022-10-14 14:00:00")
def test_domains_endpoint(client, single_domain_schema):
    resp = client.get("/domains")

    assert resp.status_code == 200
    assert resp.json() == [json.loads(single_domain_schema.json())]
