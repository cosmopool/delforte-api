import pytest

from zione.core.settings import CONNECTION, HOST, PORT, USER, PASSWORD, DB_NAME
from zione.core.exceptions import DatabaseError
from zione.infra.repositories.postgres_repository import PostgresRepository

class TestPostgresRepository:
    ap = {"time": "10:00", "date": "12-12-2021", "duration": "1:00", "ticketId": 43, "isFinished": False}
    tk = {
        # "id": 1,
        "clientName": "Roberto Barao",
        "clientAddress": "Rua David Campista, 211",
        "clientPhone": 41999000888,
        "serviceType": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False
    }

    def test_default_connection_string(self):
        repo = PostgresRepository()
        
        assert repo.connection == CONNECTION
        
    def test_custom_connection_string(self):
        connection = f"host=000 port=000 user=000 password=000 dbname=000"
        repo = PostgresRepository(connection)
        
        assert repo.connection == connection

    @pytest.mark.slow
    @pytest.mark.super_slow
    def test_no_connection_with_host_error_message(self):
        # pytest.xfail("psycopg has differents messages when it cant connect with the host")
        connection = f"host=0.0.0.1 port={PORT} user={USER} password={PASSWORD} dbname={DB_NAME}"
        repo = PostgresRepository(connection)
        res = repo.insert(self.ap, "appointments")
        
        assert res.error == DatabaseError("Error on insert")
        assert res.message == 'connection failed: database "000" does not exist'
        # assert res.error == DatabaseError('connection failed: Connection refused\n\tIs the server running on host "0.0.0.0" and accepting\n\tTCP/IP connections on port 5432?')

    def test_wrong_password_error_message(self):
        connection = f"host={HOST} port={PORT} user={USER} password=000 dbname={DB_NAME}"
        repo = PostgresRepository(connection)
        res = repo.insert(self.ap, "appointments")
        
        assert res.error == DatabaseError("Error on insert")
        assert res.message == 'connection failed: password authentication failed for user "zione"'

    def test_wrong_db_name_error_message(self):
        connection = f"host={HOST} port={PORT} user={USER} password={PASSWORD} dbname=000"
        repo = PostgresRepository(connection)
        res = repo.insert(self.ap, "appointments")
        
        assert res.error == DatabaseError("Error on insert")
        assert res.message == 'connection failed: database "000" does not exist'

    def test_wrong_user_error_message(self):
        connection = f"host={HOST} port={PORT} user=000 password={PASSWORD} dbname={DB_NAME}"
        repo = PostgresRepository(connection)
        res = repo.insert(self.ap, "appointments")
        
        assert res.error == DatabaseError("Error on insert")
        assert res.message == 'connection failed: password authentication failed for user "000"'

    # def test_no_connection_with_host_error_message_2(self):
    #     connection = f"host=1.1.1.1 port={PORT} user={USER} password={PASSWORD} dbname={DB_NAME}"
    #     repo = PostgresRepository(connection)
    #     res = repo.insert(self.ap, "appointments")
    #     
    #     assert res.error == DatabaseError("Error on insert")
    #     assert res.message == 'connection failed: password authentication failed for user "000"'
