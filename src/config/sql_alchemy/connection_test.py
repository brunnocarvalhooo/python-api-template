from sqlalchemy.engine import Engine
import pytest

from .connection import DBConnectionHandler

@pytest.mark.skip(reason="db integration test")
def teste_connect_to_db():
    db_connection_handler = DBConnectionHandler()
    assert db_connection_handler.get_engine() is None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
