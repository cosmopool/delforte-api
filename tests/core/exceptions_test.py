import pytest

from zione.core.exceptions import BaseError, DatabaseError

class TestExceptions:
    def test_default_error_is_raised_with_success(self):
        with pytest.raises(BaseError):
            raise BaseError()

    def test_default_error_to_str_method(self):
        err = BaseError("Test")

        assert isinstance(err.__str__(), str)

    def test_default_error_default_message(self):
        err = BaseError()

        assert err.__str__() == " || Generic error"

    def test_database_error_message(self):
        err = DatabaseError("No connection")

        assert err.__str__() == "Database error || No connection"

    def test_database_error_equality_with_same_(self):
        err1 = DatabaseError("No connection")
        err2 = DatabaseError("No connection")

        assert err1 == err2

    def test_database_error_equality_with_different(self):
        err1 = DatabaseError("No connection")
        err2 = DatabaseError("With connection")

        assert err1 is not err2
