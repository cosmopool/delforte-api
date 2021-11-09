# from flask_sqlalchemy import SQLAlchemy
import psycopg

# db = SQLAlchemy()

PG_URL = "postgresql://10.5.40.10:5432"
HOST = "10.5.40.10"
PORT = "5432"
USER = "postgres"
PASSWORD = "masktrum(sapiencia)19812"
DB_NAME = "test"
CONNECTION = f"host={HOST} port={PORT} user={USER} password={PASSWORD} dbname={DB_NAME}"

# with psycopg.connect(f"host={HOST} port={PORT} user={USER} password={PASSWORD} dbname={DB_NAME}") as conn:
#     conn.execute(" CREATE TABLE tickets (id bigserial PRIMARY KEY, client_name text NOT NULL, client_phone varchar(11) NOT NULL, service_type varchar(10) NOT NULL, description text NOT NULL, is_finished bool DEFAULT false NOT NULL)")
#     conn.execute(" CREATE TABLE users (id smallserial PRIMARY KEY, username varchar(80) UNIQUE NOT NULL, password text NOT NULL)")
#     conn.execute(" CREATE TABLE appointments (id bigserial PRIMARY KEY, date date NOT NULL, time time NOT NULL, duration interval NOT NULL, is_finished bool DEFAULT false, ticket_id bigserial NOT NULL)")

#     conn.execute(" INSERT INTO users (username, password) VALUES (%s, %s)", ("kaio", "kaio123"))
#     conn.execute(" INSERT INTO users (username, password) VALUES (%s, %s)", ("kaio", "kaio123"))
#     conn.execute(" INSERT INTO users (username, password) VALUES (%s, %s)", ("kaio", "kaio123"))
    
#     users = conn.execute("SELECT * FROM users").fetchall()

#     for user in users:
#         print(user)
    
#     conn.execute("DROP TABLE users")

def str_values(tuple):
    """ Print a string with `%s` for each element of a tuple. Usable for a psycopg SQL query. """
    result = []
    for element in tuple:
        result.append("%s")
    result = ", ".join(result)

    return result

# def insert(table, columns, values):
#     columns = ",".join(columns)
#     query = f"INSERT INTO {table} ({columns}) VALUES ({str_values(values)})"
#     with psycopg.connect(CONNECTION) as conn:
#         conn.execute(query, values)

def insert(table, dict):
    columns = ", ".join(dict.keys())
    values = tuple(dict.values())

    query = f"INSERT INTO {table} ({columns}) VALUES ({str_values(dict)})"

    with psycopg.connect(CONNECTION) as conn:
        result = conn.execute(query, values).pgresult.command_status

    return return_command_status(result)

def select(table, dict):
    """ Return a dictionaries of records """
    result = []
    if type(table) == type(()):
        # TODO: code real implementation to UNION
        column = dict.keys()
        value = dict.values()
        # query = f"SELECT row_to_json({ table[0] }) FROM { table[0] } WHERE { column[0] } = { value[0] } UNION SELECT row_to_json({ table[1] }) FROM { table[1] } WHERE { column[1] } = { value[1] }"
        # query = f"SELECT row_to_json({ table[0] }) FROM { table[0] } WHERE ticket_id = { value[0] } UNION SELECT row_to_json({ table[1] }) FROM { table[1] } WHERE { column[1] } = { value[1] }"
        query = f"SELECT row_to_json(app_tck) FROM (SELECT tickets.client_name, tickets.client_phone, tickets.service_type, tickets.description, appointments.date, appointments.time, appointments.duration, appointments.is_finished FROM appointments INNER JOIN tickets ON appointments.ticket_id = tickets.id) AS app_tck;"

    elif len(dict.keys()) == 1:
        column = "".join(dict.keys())
        value = "".join(dict.values())
        query = f"SELECT row_to_json({ table }) FROM { table } WHERE { column } = { value }"
        print(query)

        with psycopg.connect(CONNECTION) as conn:
            selection = conn.execute(query).fetchall()
            for record in selection:
                if record != None:
                    result.append(record[0])

        if len(result) == 0:
            raise KeyError(" No record found with given id.")
        # print(f"-------------------------- result: { result }")
        return result
    else:
        raise DataBaseImplementationError("Need to implement SELECT function with more than 1 conditional.")

def return_command_status(byte):
    byte_to_str = ''.join(map(chr, byte))
    status_list = byte_to_str.rsplit(" ")
    status = status_list[len(status_list) - 1]

    return int(status)

def delete(table, dict):
    """ Delete specific record """
    result = []
    if len(dict.keys()) == 1:
        column = "".join(dict.keys())
        value = "".join(dict.values())
        query = f"DELETE FROM { table } WHERE { column } = { value }"

        with psycopg.connect(CONNECTION) as conn:
            result = conn.execute(query).pgresult.command_status

        return return_command_status(result)
    else:
        raise DataBaseImplementationError("Need to implement SELECT function with more than 1 conditional.")

def make_update_str(record):
    keys = record.keys()
    values = record.values()
    list = []

    for key in keys:
        list.append(f"{ key } = \'{ record.get(key) }\'")

    return ", ".join(list)

def update(table, ticket_id, record):
    """ Return a dictionaries of records """
    ticket_id = ticket_id.get("id")
    columns = ", ".join(str(record.keys()))
    values = ", ".join(str(record.values()))
    query = f"UPDATE { table } SET { make_update_str(record) } WHERE id = { ticket_id }"

    with psycopg.connect(CONNECTION) as conn:
        result = conn.execute(query)
        status = return_command_status(result.pgresult.command_status)

    return status

def auth_user(table=None, dict=None, user_id=None):
    """ Return a dictionaries of records """
    result = []
    if table and dict and not user_id:
        password = str(dict.get("password"))
        username = str(dict.get("username"))
        column = "".join(dict.keys())
        value = "".join(dict.values())
        # query = f"SELECT id FROM { table } WHERE { column } = crypt('{ value }', password)"
        query = f"SELECT row_to_json(users) FROM { table } WHERE username = \'{ username }\' AND password = crypt('{ password }', password)"
        # print(f"----------------------- 1 query: { query }")
    elif user_id and not (table and dict):
        query = f"SELECT row_to_json(users) FROM users WHERE id = { user_id }"
        # print(f"----------------------- 2 query: { query }")
    else:
        return "no valid input"
    # print(query)

    with psycopg.connect(CONNECTION) as conn:
        selection = conn.execute(query).fetchall()

        for record in selection:
            # print(record)
            if record != None:
                result.append(record[0])

    if len(result) == 0:
        raise KeyError(" No record found with given id.")

    return result

def insertUser(table, dict):
    columns = ", ".join(dict.keys())
    dict_vals = tuple(dict.values())
    values = (dict_vals[0], f"crypt(\'{dict_vals[1]}\', gen_salt(\'bf\'))")
    query = f"INSERT INTO {table} ({columns}) VALUES (%s, crypt(%s, gen_salt('bf')))"

    with psycopg.connect(CONNECTION) as conn:
        result = conn.execute(query, values).pgresult.command_status

    return return_command_status(result)

