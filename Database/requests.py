from Database.models import Cider
from Database.models import async_session

from sqlalchemy import select


async def get_ciders_rus(manufacture: str, sour: str):
    async with async_session() as session:
        ciders = await session.execute(select(Cider).where(
            (Cider.sour == sour), (Cider.country == 'Россия'), (Cider.manufacture == manufacture)
        ))

        ciders_list = ciders.scalars().all()
        return ciders_list


async def get_ciders_it():
    async with async_session() as session:
        ciders = await session.execute(select(Cider).where(
         (Cider.country == 'Италия')
        ))

        ciders_list = ciders.scalars().all()
        return ciders_list


async def get_ciders_gr():
    async with async_session() as session:
        ciders = await session.execute(select(Cider).where(
         (Cider.country == 'Германия')
        ))

        ciders_list = ciders.scalars().all()
        return ciders_list


async def get_ciders_sp(sour: str, region: str):
    async with async_session() as session:
        ciders = await session.execute(select(Cider).where(
         (Cider.country == 'Испания'), (Cider.sour == sour), (Cider.region == region)
        ))

        ciders_list = ciders.scalars().all()
        return ciders_list


async def get_ciders_fr(sour: str, region: str) -> object:
    async with async_session() as session:
        ciders = await session.execute(select(Cider).where(
         (Cider.country == 'Франция'), (Cider.sour == sour), (Cider.region == region)
        ))

        ciders_list = ciders.scalars().all()
        return ciders_list


async def get_ciders_fr_brut(region: str, manufacture: str):
    async with async_session() as session:
        ciders = await session.execute(select(Cider).where(
         (Cider.country == 'Франция'), (Cider.sour == 'Brut'), (Cider.region == region),
            (Cider.manufacture == manufacture)
        ))

        ciders_list = ciders.scalars().all()
        return ciders_list


async def get_ciders_fr_sv(region: str):
    async with async_session() as session:
        ciders = await session.execute(select(Cider).where(
         (Cider.country == 'Франция'), (Cider.region == region)
        ))

        ciders_list = ciders.scalars().all()
        return ciders_list


async def get_ciders_poire(manufacture: str):
    async with async_session() as session:
        ciders = await session.execute(select(Cider).where(
         (Cider.country == 'Франция'), (Cider.sour == "Poire"), (Cider.manufacture == manufacture)
        ))

        ciders_list = ciders.scalars().all()
        return ciders_list


async def get_random_cider(id: int):
    async with async_session() as session:
        ciders = await session.execute(select(Cider).where(
            Cider.id == id
        ))

        ciders_list = ciders.scalars().all()
        return ciders_list


async def get_ciders_uk(manufacture: str, sour: str):
    async with async_session() as session:
        ciders = await session.execute(select(Cider).where(
            (Cider.sour == sour), (Cider.country == 'Англия'), (Cider.manufacture == manufacture)
        ))

        ciders_list = ciders.scalars().all()
        return ciders_list
