from .config import conn, cursor


class Dog:
    def __init__(self, name, breed, age, gender, vaccinated=False, adoption_center_id=None, id=None):
        self.id = id
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender
        self.vaccinated = vaccinated
        self.adoption_center_id = adoption_center_id

    def __repr__(self):
        return f"<Dog {self.name} {self.breed} {self.age} {self.gender} {self.vaccinated} {self.adoption_center_id}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS dogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            breed TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            vaccinated BOOLEAN NOT NULL DEFAULT 0,
            adoption_center_id INTEGER
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Dog table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS dogs;"
        cursor.execute(sql)
        conn.commit()
        print("Dog table dropped successfully")

    def save(self):
        sql = """
            INSERT INTO dogs (name, breed, age, gender, vaccinated, adoption_center_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.breed, self.age, self.gender, self.vaccinated, self.adoption_center_id))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, breed, age, gender, vaccinated=False, adoption_center_id=None):
        dog = cls(name, breed, age, gender, vaccinated, adoption_center_id)
        dog.save()
        return dog

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM dogs WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    def update(self):
        sql = """
            UPDATE dogs
            SET name = ?, breed = ?, age = ?, gender = ?, vaccinated = ?, adoption_center_id = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.breed, self.age, self.gender, self.vaccinated, self.adoption_center_id, self.id))
        conn.commit()

    def delete(self):
        sql = "DELETE FROM dogs WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()
