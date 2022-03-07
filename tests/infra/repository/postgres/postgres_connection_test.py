from zione.core.dependency_injection import make_repository
from zione.core.exceptions import DatabaseError


class TestPostgresRepository:
    ap = {"time": "10:00", "date": "12-12-2021", "duration": "1:00", "ticketId": 1, "isFinished": False}
    tk = {
        "clientName": "Roberto Barao",
        "clientAddress": "Rua David Campista, 211",
        "clientPhone": 41999000888,
        "serviceType": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False
    }
    df_connection = f"host=0.0.0.0 port=5432 user=zione password=test_pass dbname=test"


    def test_default_connection_string(self, app):
        repo = make_repository(app)
        
        assert repo.connection == self.df_connection

        
    def test_custom_connection_string(self, app):
        connection = f"host=000 port=000 user=000 password=000 dbname=000"
        app.config['CONNECTION'] = connection
        repo = make_repository(app)
        
        assert repo.connection == connection


    def test_wrong_password_error_message(self, app):
        HOST = "0.0.0.0"
        PORT = "5432"
        USER = "zione"
        DB_NAME = "test"
        connection = f"host={HOST} port={PORT} user={USER} password=000 dbname={DB_NAME}"
        app.config['CONNECTION'] = connection
        repo = make_repository(app)
        res = repo.insert(self.ap, "appointments")
        
        assert res.error == DatabaseError("Error on insert")
        assert 'password authentication failed' in res.message


    def test_wrong_db_name_error_message(self, app):
        HOST = "0.0.0.0"
        PORT = "5432"
        USER = "zione"
        PASSWORD = "test_pass"
        connection = f"host={HOST} port={PORT} user={USER} password={PASSWORD} dbname=000"
        app.config['CONNECTION'] = connection
        repo = make_repository(app)
        res = repo.insert(self.ap, "appointments")
        
        assert res.error == DatabaseError("Error on insert")
        assert 'database "000" does not exist' in res.message


    def test_wrong_user_error_message(self, app):
        HOST = "0.0.0.0"
        PORT = "5432"
        PASSWORD = "test_pass"
        DB_NAME = "test"
        connection = f"host={HOST} port={PORT} user=000 password={PASSWORD} dbname={DB_NAME}"
        app.config['CONNECTION'] = connection
        repo = make_repository(app)
        res = repo.insert(self.ap, "appointments")
        
        assert res.error == DatabaseError("Error on insert")
        assert 'password authentication failed for user "000"' in res.message
