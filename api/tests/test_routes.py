from src import __version__

from src.core.config import settings


def test_root_endpoint(client):
    resp = client.get("/")

    assert resp.status_code == 200
    assert resp.json() == {"app": settings.TITLE, "version": __version__}
