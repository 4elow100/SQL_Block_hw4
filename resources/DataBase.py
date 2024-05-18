import psycopg2
from PySide6.QtWidgets import QMessageBox


class DataBase:
    def __init__(self):
        self.create_db()

    def create_connection(self):
        self.db = psycopg2.connect(database="netology_db", user="postgres", password="1253")

    def create_db(self):
        self.create_connection()
        with self.db.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS client_db(
                id         SERIAL      PRIMARY KEY,
                last_name  VARCHAR(40) NOT NULL,
                first_name VARCHAR(40) NOT NULL,
                email      VARCHAR(80) NOT NULL,
                           UNIQUE (first_name, last_name, email)
            );
            """)
            cur.execute("""
            CREATE TABLE IF NOT EXISTS phone_db(
                id        SERIAL      PRIMARY KEY,
                client_id INTEGER     NOT NULL
                          REFERENCES client_db(id),
                phone     VARCHAR(15) NOT NULL 
                          UNIQUE
            );
            """)
        self.db.commit()
        self.db.close()

    def add_client(self, first_name, last_name, email, phone_number, phone_exists):
        self.create_connection()
        client_id = 0
        with self.db.cursor() as cur:
            cur.execute("""
            INSERT INTO client_db(last_name, first_name, email)
            VALUES (%s, %s, %s);
            """, (last_name, first_name, email))
            self.db.commit()
            cur.execute("""
            SELECT id FROM client_db
             WHERE last_name = %s
               AND first_name = %s
               AND email = %s;
            """, (last_name, first_name, email))
            client_id = cur.fetchone()
            for phone in phone_number:
                if phone_exists:
                    cur.execute("""
                    INSERT INTO phone_db(client_id, phone)
                    VALUES (%s, %s);
                    """, (client_id, phone))
            self.db.commit()
        self.db.close()

    def add_phone(self, client_id, phone_number):
        self.create_connection()
        with self.db.cursor() as cur:
            cur.execute("""
            INSERT INTO phone_db(client_id, phone)
            VALUES (%s, %s);
            """, (client_id, phone_number))
            self.db.commit()
        self.db.close()

    def edit_data_client(self, client_id, first_name, last_name, email):
        self.create_connection()
        with self.db.cursor() as cur:
            cur.execute("""
            UPDATE client_db 
               SET last_name = %s, first_name = %s, email = %s
             WHERE id = %s;
            """, (last_name, first_name, email, client_id))
            self.db.commit()
        self.db.close()

    def edit_phone(self, phone_id, phone_number):
        self.create_connection()
        with self.db.cursor() as cur:
            cur.execute("""
            UPDATE phone_db 
               SET phone = %s
             WHERE id = %s;
            """, (phone_number, phone_id))
            self.db.commit()
        self.db.close()

    def show_phone(self, client_id):
        self.create_connection()
        with self.db.cursor() as cur:
            cur.execute("""
            SELECT id, phone
              FROM phone_db
             WHERE client_id = %s;
            """, (client_id,))
            phone_data = cur.fetchall()
        self.db.close()
        return phone_data

    def delete_phone(self, phone_id):
        self.create_connection()
        with self.db.cursor() as cur:
            cur.execute("""
            DELETE FROM phone_db
             WHERE id = %s;
            """, (phone_id,))
            self.db.commit()
        self.db.close()

    def delete_client(self, client_id):
        self.create_connection()
        with self.db.cursor() as cur:
            cur.execute("""
            DELETE FROM phone_db
             WHERE client_id = %s;
            """, (client_id,))
            cur.execute("""
            DELETE FROM client_db
             WHERE id = %s;
            """, (client_id,))
            self.db.commit()
        self.db.close()

    def search_client(self, first_name, last_name, email, phone_number):
        self.create_connection()
        with self.db.cursor() as cur:
            if phone_number:
                cur.execute("""
                SELECT cd.id
                  FROM client_db AS cd
                       JOIN phone_db AS pd
                         ON cd.id = pd.client_id
                 WHERE pd.phone LIKE %s
                   AND cd.last_name LIKE %s
                   AND cd.first_name LIKE %s
                   AND cd.email LIKE %s;
                """, (phone_number + '%', last_name + '%', first_name + '%', email + '%'))
            else:
                cur.execute("""
                SELECT id
                  FROM client_db
                 WHERE last_name LIKE %s
                   AND first_name LIKE %s
                   AND email LIKE %s;
                """, (last_name + '%', first_name + '%', email + '%'))
            client_id = cur.fetchall()
        self.db.close()
        return client_id

    def show_data(self):
        self.create_connection()
        data = []
        with self.db.cursor() as cur:
            cur.execute("""
            SELECT id 
              FROM client_db;
            """)
            client_id = cur.fetchall()
            for ids in client_id:
                client_list = []
                cur.execute("""
                SELECT *
                  FROM client_db
                 WHERE id = %s;
                """, (ids,))
                client_list.append(cur.fetchall())
                cur.execute("""
                SELECT phone
                  FROM phone_db
                 WHERE client_id = %s;
                """, (ids,))
                client_list.append(cur.fetchall())
                data.append(client_list)
        self.db.close()
        return data
