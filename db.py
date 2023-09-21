import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, event, inspect
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker


load_dotenv(".envs/.env_db")


class Model(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


#########################
# NOT ASYNC APPLICATION #
#########################
# print('Database URL:', os.getenv('DATABASE_URL'))
# engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
# Session = sessionmaker(engine)

#####################
# ASYNC APPLICATION #
#####################
engine = create_async_engine(os.getenv("DATABASE_URL"))
Session = async_sessionmaker(engine, expire_on_commit=False)


@event.listens_for(Model, "init", propagate=True)
def init_relationships(tgt, arg, kw):
    mapper = inspect(tgt.__class__)
    for arg in mapper.relationships:
        if arg.collection_class is None and arg.uselist:
            continue  # skip write-only and similar relationships
        if arg.key not in kw:
            kw.setdefault(arg.key, None if not arg.uselist else arg.collection_class())
