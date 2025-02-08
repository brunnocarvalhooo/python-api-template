import uuid
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from src.models.sqlite.settings.base import Base


class UsersTable(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    whatsapp = Column(String, nullable=False)
    avatar = Column(String, nullable=True)
    password = Column(String, nullable=False)
    status = Column(Boolean, default=True)
    active = Column(Boolean, default=False)

    def __repr__(self):
        return "Users [" + ", ".join([
            f"id={self.id}",
            f"name={self.name}",
            f"email={self.email}",
            f"whatsapp={self.whatsapp}",
            f"avatar={self.avatar}",
            f"status={self.status}",
            f"active={self.active}"
        ]) + "]"
