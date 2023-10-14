import json

import pytest
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
@pytest.mark.parametrize(
    "available, expected_total, pages", [(True, 1, 1), (False, 0, 0)]
)
def test_domains_with_filter_available(
    client, single_domain_schema, available, expected_total, pages
):
    resp = client.get(f"/domains?available={available}")

    assert resp.status_code == 200
    assert resp.json() == {
        "items": [json.loads(single_domain_schema.json())] if available else [],
        "total": expected_total,
        "page": 1,
        "pages": pages,
        "size": 50,
    }


@freeze_time("2022-10-14 14:00:00")
def test_domains_with_filter_status(client, single_domain_schema):
    resp = client.get("/domains?status=active")

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
