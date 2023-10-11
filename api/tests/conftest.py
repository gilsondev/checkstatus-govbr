import pytest
from fastapi.testclient import TestClient
from freezegun import freeze_time
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src import models
from src import schemas
from src.core.config import settings
from src.core.database import get_db
from src.main import app


@pytest.fixture(scope="session")
def engine():
    return create_engine(settings.TEST_DATABASE_URL)


@pytest.fixture(scope="session")
def database(engine):
    models.Base.metadata.create_all(engine)
    yield engine

    with engine.connect() as conn:
        result = conn.execute(
            "SELECT tablename FROM pg_tables WHERE schemaname='public'"
        )
        tables = [row[0] for row in result]
        for table in tables:
            conn.execute(f"DROP TABLE IF EXISTS {table} CASCADE")


@pytest.fixture(scope="function")
def db_session(database):
    connection = database.connect()
    transaction = connection.begin()

    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(db_session):
    def _get_db_override():
        return db_session

    app.dependency_overrides[get_db] = _get_db_override
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def domain_raw():
    return {
        "domain": "gdf.gov.br",
        "slug": "gdf",
        "document": "001.175.497/0001-41",
        "document_normalized": "001175497000141",
        "organization": "Agencia Brasileira de Inteligencia",
        "organization_normalized": "agencia brasileira de inteligencia",
        "agent": "Rodrigo Bastos Vasconcelos Teperino",
        "agent_normalized": "rodrigo bastos vasconcelos teperino",
        "nameservers": ["dns1.gdfnet.df.gov.br", "dns2.df.gov.br"],
        "department": "Suporte Técnico - CODEPLAN",
        "department_normalized": "suporte tecnico - codeplan",
        "department_email": "suporte@gdfnet.df.gov.br",
        "status": ["active"],
        "available": True,
        "registered_at": "2006-09-26T17:47:00.000",
        "refreshed_at": "2021-06-23T17:09:00.000",
        "created_at": "2022-05-01T15:00:00.000",
        "updated_at": "2022-06-04T09:00:00.000",
    }


@freeze_time("2022-10-14 14:00:00")
@pytest.fixture
def single_domain(db_session, domain_raw):
    domain_raw.pop("created_at")
    domain_raw.pop("updated_at")
    domain = models.Domain(**domain_raw)
    db_session.add(domain)
    db_session.commit()
    db_session.flush()
    db_session.refresh(domain)

    return domain


@pytest.fixture
def single_domain_schema(single_domain):
    return schemas.DomainItem.from_orm(single_domain)
