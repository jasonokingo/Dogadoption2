# models/adopter.py

from .config import conn, cursor

class Adopter:
    def __init__(self, name, contact, id=None):
        self.id = id
        self.name = name
        self.contact = contact

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS adopters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Adopter table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS adopters"
        cursor.execute(sql)
        conn.commit()
        print("Adopter table dropped successfully")

    def save(self):
        if self.id:
            sql = """
                UPDATE adopters SET name=?, contact=?
                WHERE id=?
            """
            cursor.execute(sql, (self.name, self.contact, self.id))
        else:
            sql = """
                INSERT INTO adopters (name, contact)
                VALUES (?, ?)
            """
            cursor.execute(sql, (self.name, self.contact))
            self.id = cursor.lastrowid
        conn.commit()

    @classmethod
    def create(cls, name, contact):
        adopter = cls(name, contact)
        adopter.save()
        return adopter

    @classmethod
    def find_by_id(cls, adopter_id):
        sql = "SELECT * FROM adopters WHERE id = ?"
        cursor.execute(sql, (adopter_id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    def delete(self):
        if self.id is not None:
            sql = "DELETE FROM adopters WHERE id=?"
            cursor.execute(sql, (self.id,))
            conn.commit()

    @classmethod
    def find_all(cls):
        sql = "SELECT * FROM adopters"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]
from .config import conn, cursor

class Adopter:
    def __init__(self, name, contact, id=None):
        self.id = id
        self.name = name
        self.contact = contact

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS adopters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Adopter table created successfully")

    def save(self):
        if self.id:
            sql = """
                UPDATE adopters SET name=?, contact=?
                WHERE id=?
            """
            cursor.execute(sql, (self.name, self.contact, self.id))
        else:
            sql = """
                INSERT INTO adopters (name, contact)
                VALUES (?, ?)
            """
            cursor.execute(sql, (self.name, self.contact))
            self.id = cursor.lastrowid
        conn.commit()

    @classmethod
    def create(cls, name, contact):
        adopter = cls(name, contact)
        adopter.save()
        return adopter

    @classmethod
    def find_by_id(cls, adopter_id):
        sql = "SELECT * FROM adopters WHERE id = ?"
        cursor.execute(sql, (adopter_id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    def delete(self):
        if self.id is not None:
            sql = "DELETE FROM adopters WHERE id=?"
            cursor.execute(sql, (self.id,))
            conn.commit()

    @classmethod
    def find_all(cls):
        sql = "SELECT * FROM adopters"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]
