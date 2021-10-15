from sqlalchemy import create_engine, select, MetaData, Table, and_
from sqlalchemy.dialects.mssql import try_cast
import pyodbc
import simplejson as json
import decimal, datetime
from sqlalchemy.sql.expression import column
from conf import Connection

def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return int(obj)

pyodbc.pooling = False

# don't use the engine before pooling is set to False
def recupera_dados(name_table):
    engine = create_engine(Connection.connection_url)
    metadata = MetaData(bind=None)
    smt = select(
        Table(name_table, 
            metadata,
            autoload=True, 
            autoload_with=engine)
    )

    connection = engine.connect()

    results = connection.execute(smt).fetchall()
    connection.close()

    return json.dumps([dict(r) for r in results],default=alchemyencoder)

def recupera_dados_id(name_table, id):
    engine = create_engine(Connection.connection_url)
    metadata = MetaData(bind=None)

    smt = select(
        Table(name_table, 
            metadata,
            autoload=True, 
            autoload_with=engine)
    ).where(column('id')==id)

    connection = engine.connect()

    results = connection.execute(smt).fetchall()
    connection.close()
    return json.dumps([dict(r) for r in results],  ensure_ascii=False, default=alchemyencoder)



 