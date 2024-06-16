from .config import conn, cursor

class Dog:
    def __init__(self, name, breed, age, gender, vaccinated, id=None):
        self.id = id
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender
        self.vaccinated = vaccinated

    @classmethod
    def create_table(cls):
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

    def save(self):
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

    @classmethod
    def create(cls, name, breed, age, gender, vaccinated):
        dog = cls(name, breed, age, gender, vaccinated)
        dog.save()
        return dog

    @classmethod
    def find_by_id(cls, dog_id):
        sql = "SELECT * FROM dogs WHERE id = ?"
        cursor.execute(sql, (dog_id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    def delete(self):
        if self.id is not None:
            sql = "DELETE FROM dogs WHERE id=?"
            cursor.execute(sql, (self.id,))
            conn.commit()

    @classmethod
    def find_all(cls):
        sql = "SELECT * FROM dogs"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]
