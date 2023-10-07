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
    assert resp.json() == {
        "items": [json.loads(single_domain_schema.json())],
        "total": 1,
        "page": 1,
        "pages": 1,
        "size": 50,
    }


@freeze_time("2022-10-14 14:00:00")
def test_search_domains_endpoint(client, single_domain_schema):
    resp = client.get("/domains?search=gdf")

    assert resp.status_code == 200
    assert resp.json() == {
        "items": [json.loads(single_domain_schema.json())],
        "total": 1,
        "page": 1,
        "pages": 1,
        "size": 50,
    }


@freeze_time("2022-10-14 14:00:00")
def test_search_unknown_domain(client, single_domain_schema):
    resp = client.get("/domains?search=nonexist")

    assert resp.status_code == 200
    assert resp.json() == {
        "items": [],
        "total": 0,
        "page": 1,
        "pages": 0,
        "size": 50,
    }
