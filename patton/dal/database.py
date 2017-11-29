from contextlib import contextmanager

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy_utils.functions import drop_database, create_database, database_exists

from ..config import DB_URL


engine = sqlalchemy.create_engine(DB_URL, client_encoding='utf8', use_batch_mode=True)


Base = declarative_base()


@contextmanager
def session_ctx():
    session = Session(bind=engine)
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def drop():
    if database_exists(engine.url):
        drop_database(engine.url)


def create():
    if not database_exists(engine.url):
        create_database(engine.url)

    # INFO: we need to `load` to Base the Models
    from . import models  # noqa

    Base.metadata.create_all(engine)


def recreate():
    drop()
    create()
