from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class ProjectUser(Base):
    __tablename__ = 'users'
    
    discord_user_id: Mapped[int] = mapped_column(primary_key=True)
    osu_user_id: Mapped[int] = mapped_column()