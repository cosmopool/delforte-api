import psycopg
from zione.settings import CONNECTION


def str_values(tuple):
    """ Print a string with `%s` for each element of a tuple. Usable for a psycopg SQL query. """
    result = []
    for _ in tuple:
        result.append("%s")
    result = ", ".join(result)

    return result

def insert(table, dict):
    columns = ", ".join(dict.keys())
    values = tuple(dict.values())

    query = f"WITH entry AS (INSERT INTO {table} ({columns}) VALUES ({str_values(dict)}) RETURNING id) SELECT row_to_json(entry) FROM entry"

    with psycopg.connect(CONNECTION) as conn:
        result = conn.execute(query, values).fetchall()

    print(result[0][0])
    return result[0][0]['id']

def select(table, dict):
    """ Return a dictionaries of records """
    result = []
    if type(table) == type(()):
        # print(f" -------------- here 1123")
        # TODO: code real implementation to UNION
        # column = dict.keys()
        # value = dict.values()
        # query = f"SELECT row_to_json({ table[0] }) FROM { table[0] } WHERE { column[0] } = { value[0] } UNION SELECT row_to_json({ table[1] }) FROM { table[1] } WHERE { column[1] } = { value[1] }"
        # query = f"SELECT row_to_json({ table[0] }) FROM { table[0] } WHERE ticket_id = { value[0] } UNION SELECT row_to_json({ table[1] }) FROM { table[1] } WHERE { column[1] } = { value[1] }"
        # TODO: need to filer records by *dict* argument. right now, it prints every record
        query = f"SELECT row_to_json(app_tck) FROM (SELECT tickets.client_name, tickets.client_phone, tickets.client_address, tickets.service_type, tickets.description, appointments.date, appointments.time, appointments.duration, appointments.id, appointments.ticket_id, tickets.is_finished FROM appointments INNER JOIN tickets ON appointments.ticket_id = tickets.id) AS app_tck;"
        # print(f"----------------------- query: {query}")

    elif len(dict.keys()) == 1:
        # print(f" -------------- here 2231")
        column = "".join(dict.keys())
        value = "".join(dict.values())
        query = f"SELECT row_to_json({ table }) FROM { table } WHERE { column } { value }"
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
    # values = record.values()
    list = []

    for key in keys:
        list.append(f"{ key } = \'{ record.get(key) }\'")

    return ", ".join(list)

def update(table, dict, ticket_id):
    """ Return a dictionaries of records """
    # ticket_id = ticket_id.get("id")
    # columns = ", ".join(str(dict.keys()))
    # values = ", ".join(str(dict.values()))
    query = f"UPDATE { table } SET { make_update_str(dict) } WHERE id = { ticket_id }"

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
        # column = "".join(dict.keys())
        # value = "".join(dict.values())
        # query = f"SELECT id FROM { table } WHERE { column } = crypt('{ value }', password)"
        query = f"SELECT row_to_json(users) FROM { table } WHERE username = \'{ username }\' AND password = crypt('{ password }', password)"
        # print(f"----------------------- 1 query: { query }")
    elif user_id and not (table and dict):
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

def insert_user(table, dict):
    columns = ", ".join(dict.keys())
    dict_vals = tuple(dict.values())
    values = (dict_vals[0], f"crypt(\'{dict_vals[1]}\', gen_salt(\'bf\'))")
    query = f"INSERT INTO {table} ({columns}) VALUES (%s, crypt(%s, gen_salt('bf')))"

    with psycopg.connect(CONNECTION) as conn:
        result = conn.execute(query, values).pgresult.command_status

    return return_command_status(result)

