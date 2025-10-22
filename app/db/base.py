"""
Import all SQLAlchemy models here so Alembic can discover them automatically.
"""

from app.db.base_class import Base  # noqa: F401
from app.models.student import Student  # noqa: F401
