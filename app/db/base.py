# We're import these so Base gets them before Alembic tries to import them
from app.db.base_class import Base
from app.models.user import User
