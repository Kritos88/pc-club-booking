from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from api.database.models import PC
from api.schemas.pc import PCCreate


async def get_all_pcs(db : AsyncSession):
    result = await db.execute(select(PC))
    return result.scalars().all()



async def create_pc(db : AsyncSession, pc_data : PCCreate):
    new_pc = PC(**pc_data.model_dump())
    db.add(new_pc)
    await db.commit()
    await db.refresh(new_pc)
    return new_pc