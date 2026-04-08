from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.product_model import Item


async def get_items(db: AsyncSession):
    result = await db.execute(select(Item))
    return result.scalars().all()


async def get_item(db: AsyncSession, item_id: int):
    result = await db.execute(select(Item).where(Item.id == item_id))
    return result.scalar_one_or_none()


async def create_item(db: AsyncSession, item):
    new_item = Item(name=item.name, price=item.price)
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item


async def update_item(db: AsyncSession, item_id: int, item):
    result = await db.execute(select(Item).where(Item.id == item_id))
    db_item = result.scalar_one_or_none()

    if not db_item:
        return None

    db_item.name = item.name
    db_item.price = item.price

    await db.commit()
    await db.refresh(db_item)
    return db_item


async def delete_item(db: AsyncSession, item_id: int):
    result = await db.execute(select(Item).where(Item.id == item_id))
    db_item = result.scalar_one_or_none()

    if not db_item:
        return None

    await db.delete(db_item)
    await db.commit()
    return {"message": "Deleted successfully"}