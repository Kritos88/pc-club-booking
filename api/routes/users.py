from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.users import UserOut, UserCreate
from api.database.engine import get_db
from api.queries.users import get_user_by_tg_id, create_user

router = APIRouter(prefix='/users', tags = ['Users'])


@router.post('/auth', response_model=UserOut)
async def auth_user(user_data : UserCreate, db : AsyncSession = Depends(get_db)):
    user = await get_user_by_tg_id(db, user_data.td_id)
    if user:
        return user
    new_user = await create_user(db, user_data)
    return new_user