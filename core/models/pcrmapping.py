from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class ProjectMember(Base):
    __tablename__ = 'users'
    
    discord_id: Mapped[int] = mapped_column(primary_key=True)
    osu_id: Mapped[int] = mapped_column()
    
    def __repr__(self) -> str:
        return f"ProjectMember(discord_id={self.discord_id}, osu_id={self.osu_id})"