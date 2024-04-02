from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker

engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3", echo=True)
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Cider(Base):
    __tablename__ = 'ciders'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    sour: Mapped[str] = mapped_column()
    alco: Mapped[str] = mapped_column()
    manufacture: Mapped[str] = mapped_column()
    country: Mapped[str] = mapped_column()
    region: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
