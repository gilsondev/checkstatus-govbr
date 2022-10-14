from src.schemas import DomainItem


def test_domain_item_schema(domain_raw):
    domain = DomainItem(**domain_raw)

    assert domain is not None
    assert {
        "domain",
        "slug",
        "document",
        "organization",
        "agent",
        "registered_at",
        "refreshed_at",
        "created_at",
        "updated_at",
    } == domain.__fields__.keys()
