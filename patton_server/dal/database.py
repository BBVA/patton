import sqlalchemy
import os.path as op

from sqlalchemy.ext.declarative import declarative_base

# engine = sqlalchemy.create_engine(DB_URL,
#                                   client_encoding='utf8',
#                                   use_batch_mode=True)


async def create(db_pool):
    tables_def = open(op.join(op.dirname(__file__),
                              "create_tables.sql"), "r").read()

    async with db_pool.acquire() as con:
        # Create tables
        await con.execute(tables_def)


async def check_if_db_already_created(db_pool):
    async with db_pool.acquire() as con:
        # Create tables
        resp = await con.fetchrow("""SELECT EXISTS (
   SELECT 1
   FROM   information_schema.tables 
   WHERE  table_schema = 'public'
   AND    table_name = 'prod'
   );""")
        return resp[0]


Base = declarative_base()
