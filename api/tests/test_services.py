from src.services import DomainService


def test_fetch_domains(db_session, single_domain):
    service = DomainService(db_session)
    domains = service.fetch().all()

    assert len(domains) > 0
    assert domains[0].domain == single_domain.domain
    assert domains[0].slug == single_domain.slug
