import psycopg

from zione.infra.datasouces_interface.datasouce_interface import DatasourceInterface
from zione.settings import CONNECTION

class PostgresDatasource(DatasourceInterface):
    """Interface for all datasources classes"""

    def _make_update_str(self, record):
        keys = record.keys()
        # values = record.values()
        list = []

        for key in keys:
            list.append(f"\"{ key }\" = \'{ record.get(key) }\'")

        return ", ".join(list)

    def _return_command_status(self, byte):
        byte_to_str = ''.join(map(chr, byte))
        status_list = byte_to_str.rsplit(" ")
        status = status_list[len(status_list) - 1]

        return int(status)

    def _str_values(self, tuple):
        """Print a string with `%s` for each element of a tuple. Usable for a psycopg SQL query."""
        result = []
        for _ in tuple:
            result.append("%s")
        result = ", ".join(result)

        return result

    def insert(self, record, table):
        """Add an record to the database"""

        table = table + "_view"
        columns = []

        # raise ValueError('Hiheihihi deu ruiM!')

        # print(" ------------------- insert", dict)

        for col in record.keys():
            columns.append(f'"{col}"')

        columns = ", ".join(columns)
        values = tuple(record.values())

        query = f"WITH entry AS (INSERT INTO {table} ({columns}) VALUES ({self._str_values(record)}) RETURNING id) SELECT row_to_json(entry) FROM entry"

        with psycopg.connect(CONNECTION) as conn:
            result = conn.execute(query, values).fetchall()

        # print(result[0][0])
        return result[0][0]["id"]

    def delete(self, record, table):
        """Remove an record from the database"""
        result = []
        if len(record.keys()) == 1:
            column = "".join(record.keys())
            value = "".join(record.values())
            query = f"DELETE FROM { table } WHERE { column } = { value }"

            with psycopg.connect(CONNECTION) as conn:
                result = conn.execute(query).pgresult.command_status

            return self._return_command_status(result)
        else:
            raise DataBaseImplementationError("Need to implement SELECT function with more than 1 conditional.")

    def update(self, record, table):
        """Edit an record in the database"""
        table = f"{table}_view"
        if not entryId:
            ticketId = record.get("id")
        # ticketId = ticketId.get("id")
        # columns = ", ".join(str(record.keys()))
        # values = ", ".join(str(record.values()))
        # TODO: need to test to see if reschedule is working
        query = f"UPDATE { table } SET { self._make_update_str(record) } WHERE id = { ticketId }"

        with psycopg.connect(CONNECTION) as conn:
            result = conn.execute(query)
            status = self._return_command_status(result.pgresult.command_status)

        return status

    def select(self, record, table):
        """Fetch an record from the database"""
        result = []
        table = table + "_view"
        if type(table) == type(()):
            # print(f" -------------- here 1123")
            # TODO: code real implementation to UNION
            # TODO: need to filer records by *record* argument. right now, it prints every record
            query = "SELECT row_to_json(entry_view) FROM entry_view"

        elif len(record.keys()) == 1:
            # print(f" -------------- here 2231")
            column = "".join(record.keys())
            value = "".join(record.values())
            query = f"SELECT row_to_json({ table }) FROM { table } WHERE \"{ column }\" { value }"
            # print(query)

        # print(f"-------------------------------------------------- query: { query }")
        with psycopg.connect(CONNECTION) as conn:
            selection = conn.execute(query).fetchall()
            for record in selection:
                if record != None:
                    result.append(record[0])
            # print(f"-------------------------------------------------- here: { selection }")
            # print(f"-------------------------------------------------- here: { record }")
            # print(f"-------------------------------------------------- here: { query }")

        if len(result) == 0:
            raise KeyError(" No record found with given id.")

        # print(f"-------------------------- result: { result }")
        return result

    def insert_user(self, record, table):
        columns = ", ".join(record.keys())
        record_vals = tuple(record.values())
        values = (record_vals[0], f"crypt(\'{record_vals[1]}\', gen_salt(\'bf\'))")
        query = f"INSERT INTO {table} ({columns}) VALUES (%s, crypt(%s, gen_salt('bf')))"

        with psycopg.connect(CONNECTION) as conn:
            result = conn.execute(query, values).pgresult.command_status

        return self._return_command_status(result)

    def auth_user(table=None, record=None, user_id=None):
        """ Return a recordionaries of records """
        result = []
        if table and record and not user_id:
            password = str(record.get("password"))
            username = str(record.get("username"))
            # column = "".join(record.keys())
            # value = "".join(record.values())
            # query = f"SELECT id FROM { table } WHERE { column } = crypt('{ value }', password)"
            query = f"SELECT row_to_json(users) FROM { table } WHERE username = \'{ username }\' AND password = crypt('{ password }', password)"
            # print(f"----------------------- 1 query: { query }")
        elif user_id and not (table and record):
            query = f"SELECT row_to_json(users) FROM users WHERE id = { user_id }"
            # print(f"----------------------- 2 query: { query }")
        else:
            return "no valid input"
        # print(f"----------------- query: {query}")

        with psycopg.connect(CONNECTION) as conn:
            selection = conn.execute(query).fetchall()

            for record in selection:
                # print(record)
                if record != None:
                    result.append(record[0])

        if len(result) == 0:
            raise KeyError(" No record found with given id.")

        return result
