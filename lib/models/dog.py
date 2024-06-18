# models/dog.py

from .config import conn, cursor
import sqlite3

class Dog:
    def __init__(self, id, name, breed, age, gender, vaccinated):
        self.id = id
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender
        self.vaccinated = vaccinated

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Breed: {self.breed}, Age: {self.age}, Gender: {self.gender}, Vaccinated: {self.vaccinated}"

    @classmethod
    def create_table(cls):
        try:
            sql = """
                CREATE TABLE IF NOT EXISTS dogs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    breed TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    gender TEXT NOT NULL,
                    vaccinated BOOLEAN NOT NULL
                )
            """
            cursor.execute(sql)
            conn.commit()
            print("Dog table created successfully")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def save(self):
        try:
            if self.id:
                sql = """
                    UPDATE dogs SET name=?, breed=?, age=?, gender=?, vaccinated=?
                    WHERE id=?
                """
                cursor.execute(sql, (self.name, self.breed, self.age, self.gender, self.vaccinated, self.id))
            else:
                sql = """
                    INSERT INTO dogs (name, breed, age, gender, vaccinated)
                    VALUES (?, ?, ?, ?, ?)
                """
                cursor.execute(sql, (self.name, self.breed, self.age, self.gender, self.vaccinated))
                self.id = cursor.lastrowid
            conn.commit()
            print("Dog saved successfully")
        except sqlite3.Error as e:
            print(f"Error saving dog: {e}")

    @classmethod
    def create(cls, name, breed, age, gender, vaccinated):
        try:
            dog = cls(None, name, breed, age, gender, vaccinated)
            dog.save()
            return dog
        except sqlite3.Error as e:
            print(f"Error creating dog: {e}")
            return None

    @classmethod
    def find_by_id(cls, dog_id):
        try:
            sql = "SELECT * FROM dogs WHERE id = ?"
            cursor.execute(sql, (dog_id,))
            row = cursor.fetchone()
            return cls(*row) if row else None
        except sqlite3.Error as e:
            print(f"Error finding dog by ID: {e}")
            return None

    def delete(self):
        try:
            if self.id is not None:
                sql = "DELETE FROM dogs WHERE id=?"
                cursor.execute(sql, (self.id,))
                conn.commit()
                print("Dog deleted successfully")
        except sqlite3.Error as e:
            print(f"Error deleting dog: {e}")

    @classmethod
    def select_dogs(cls):
        try:
            sql = "SELECT * FROM dogs"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [cls(*row) for row in rows]
        except sqlite3.Error as e:
            print(f"Error selecting dogs: {e}")
            return []

# Additional validations and error handling can be added as per your application's requirements.
