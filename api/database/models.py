from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, Integer, String, Boolean, DateTime, func
from datetime import datetime

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int | None] = mapped_column(BigInteger, unique=True, index = True)
    username: Mapped[str | None] = mapped_column(String(255), unique=True)
    full_name: Mapped[str | None] = mapped_column(String(255))
    hashed_password: Mapped[str | None] = mapped_column(String(255))
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

class PC(Base):
    __tablename__ = "pcs"
    id: Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(255), unique=True, index = True)
    price_per_hour : Mapped[int] = mapped_column(Integer)
    status : Mapped[str] = mapped_column(String(20), default='free')