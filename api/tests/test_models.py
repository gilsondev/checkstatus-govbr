from src.models import Domain


def test_domain_model(domain_raw):
    domain = Domain(**domain_raw)
    assert domain is not None


def test_new_domain_data(db_session, domain_raw):
    domain = Domain(**domain_raw)
    db_session.add(domain)
    db_session.commit()
    db_session.refresh(domain)

    assert domain.id == 1
