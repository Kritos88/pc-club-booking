from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from api.database.models import User
from api.schemas.users import UserCreate


async def get_user_by_tg_id(db:AsyncSession, tg_id : int) -> User | None:
    result = await db.execute(select(User).where(User.tg_id == tg_id))
    return result.scalar_one_or_none

async def create_user(db:AsyncSession, user : UserCreate) -> User:
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user