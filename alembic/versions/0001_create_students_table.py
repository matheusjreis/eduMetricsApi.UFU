from __future__ import annotations

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0001_create_students_table"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "students",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True, unique=True),
    )
    op.create_index(op.f("ix_students_id"), "students", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_students_id"), table_name="students")
    op.drop_table("students")
