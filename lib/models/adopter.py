# models/adopter.py

from .config import conn, cursor
import sqlite3

class Adopter:
    def __init__(self, id, name, contact):
        self.id = id
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Contact: {self.contact}"

    @classmethod
    def create_table(cls):
        try:
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
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def save(self):
        try:
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
            print("Adopter saved successfully")
        except sqlite3.Error as e:
            print(f"Error saving adopter: {e}")

    @classmethod
    def create(cls, name, contact):
        try:
            adopter = cls(None, name, contact)
            adopter.save()
            return adopter
        except sqlite3.Error as e:
            print(f"Error creating adopter: {e}")
            return None

    @classmethod
    def find_by_id(cls, adopter_id):
        try:
            sql = "SELECT * FROM adopters WHERE id = ?"
            cursor.execute(sql, (adopter_id,))
            row = cursor.fetchone()
            return cls(*row) if row else None
        except sqlite3.Error as e:
            print(f"Error finding adopter by ID: {e}")
            return None

    def delete(self):
        try:
            if self.id is not None:
                sql = "DELETE FROM adopters WHERE id=?"
                cursor.execute(sql, (self.id,))
                conn.commit()
                print("Adopter deleted successfully")
        except sqlite3.Error as e:
            print(f"Error deleting adopter: {e}")

    @classmethod
    def select_adopters(cls):
        try:
            sql = "SELECT * FROM adopters"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [cls(*row) for row in rows]
        except sqlite3.Error as e:
            print(f"Error selecting adopters: {e}")
            return []
