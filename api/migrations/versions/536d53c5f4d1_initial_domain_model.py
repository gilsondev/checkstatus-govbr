"""Initial domain model

Revision ID: 536d53c5f4d1
Revises: 
Create Date: 2022-10-13 21:51:41.766938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "536d53c5f4d1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "domains",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("domain", sa.String(length=256), nullable=False),
        sa.Column("slug", sa.String(length=100), nullable=False),
        sa.Column("document", sa.String(length=20), nullable=True),
        sa.Column("organization", sa.String(length=256), nullable=False),
        sa.Column("agent", sa.String(length=256), nullable=True),
        sa.Column("registered_at", sa.DateTime(), nullable=False),
        sa.Column("refreshed_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("domain"),
    )
    op.create_index(op.f("ix_domains_id"), "domains", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_domains_id"), table_name="domains")
    op.drop_table("domains")
    # ### end Alembic commands ###
