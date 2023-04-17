# Создайте программу для управления клиентами на Python.
#
# Требуется хранить персональную информацию о клиентах:
#
# имя,
# фамилия,
# email,
# телефон.
# Сложность в том, что телефон у клиента может быть не один,
# а два, три и даже больше. А может и вообще не быть телефона,
# например, он не захотел его оставлять.
#
# Вам необходимо разработать структуру БД для хранения информации
# и несколько функций на Python для управления данными.
#
# Функция, создающая структуру БД (таблицы).
# Функция, позволяющая добавить нового клиента.
# Функция, позволяющая добавить телефон для существующего клиента.
# Функция, позволяющая изменить данные о клиенте.
# Функция, позволяющая удалить телефон для существующего клиента.
# Функция, позволяющая удалить существующего клиента.
# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
# Функции выше являются обязательными, но это не значит, что должны быть только они.
# При необходимости можете создавать дополнительные функции и классы.
#
# Также предоставьте код, демонстрирующий работу всех написанных функций.
#
# Результатом работы будет .py файл.

import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                phones VARCHAR(255)[]
            );
        """)

def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO clients (first_name, last_name, email, phones) 
            VALUES (%s, %s, %s, %s) RETURNING id;
        """, (first_name, last_name, email, phones))
        client_id = cur.fetchone()[0]
    return client_id

def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
            UPDATE clients SET phones = array_append(phones, %s) WHERE id = %s;
        """, (phone, client_id))

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    with conn.cursor() as cur:
        if first_name is not None:
            cur.execute("UPDATE clients SET first_name = %s WHERE id = %s;", (first_name, client_id))
        if last_name is not None:
            cur.execute("UPDATE clients SET last_name = %s WHERE id = %s;", (last_name, client_id))
        if email is not None:
            cur.execute("UPDATE clients SET email = %s WHERE id = %s;", (email, client_id))
        if phones is not None:
            cur.execute("UPDATE clients SET phones = %s WHERE id = %s;", (phones, client_id))

def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
            UPDATE clients SET phones = array_remove(phones, %s) WHERE id = %s;
        """, (phone, client_id))

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM clients WHERE id = %s;", (client_id,))

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        if phone is not None:
            cur.execute("SELECT * FROM clients WHERE %s = ANY (phones);", (phone,))
        elif email is not None:
            cur.execute("SELECT * FROM clients WHERE email = %s;", (email,))
        elif first_name is not None and last_name is not None:
            cur.execute("SELECT * FROM clients WHERE first_name = %s AND last_name = %s;", (first_name, last_name))
        elif first_name is not None:
            cur.execute("SELECT * FROM clients WHERE first_name = %s;", (first_name,))
        elif last_name is not None:
            cur.execute("SELECT * FROM clients WHERE last_name = %s;", (last_name,))
        else:
            cur.execute("SELECT * FROM clients;")
        return cur.fetchall()


with psycopg2.connect(database="postgres", user="postgres", password="postgres") as conn:
    create_db(conn)

    client_id = add_client(conn, "AAA", "BBB", "AAABBB@gmail.com", ["123456789", "987654321"])
    print("Added client with id:", client_id)

    add_phone(conn, client_id, "1122334455")
    print("Added phone for client:", client_id)

    change_client(conn, client_id, first_name="ccc", email="cccbbbe@gmail.com")
    print("Changed client's data:", client_id)

    delete_phone(conn, client_id, "5544332211")
    print("Deleted phone from client:", client_id)

    delete_client(conn, client_id)
    print("Deleted client:", client_id)

    clients = find_client(conn, first_name="ccc")
    print("Found clients:", clients)

conn.close()