# models/adoption.py

from .config import conn, cursor

class Adoption:
    def __init__(self, dog_id, adopter_id, adoption_date, returned, id=None):
        self.id = id
        self.dog_id = dog_id
        self.adopter_id = adopter_id
        self.adoption_date = adoption_date
        self.returned = returned

    def __str__(self):
        return (f"ID: {self.id}, Dog ID: {self.dog_id}, Adopter ID: {self.adopter_id}, "
                f"Adoption Date: {self.adoption_date}, Returned: {self.returned}")


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS adoptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dog_id INTEGER NOT NULL,
                adopter_id INTEGER NOT NULL,
                adoption_date TEXT NOT NULL,
                returned BOOLEAN NOT NULL,
                FOREIGN KEY (dog_id) REFERENCES dogs(id),
                FOREIGN KEY (adopter_id) REFERENCES adopters(id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Adoption table created successfully")

    def save(self):
        if self.id:
            sql = """
                UPDATE adoptions SET dog_id=?, adopter_id=?, adoption_date=?, returned=?
                WHERE id=?
            """
            cursor.execute(sql, (self.dog_id, self.adopter_id, self.adoption_date, self.returned, self.id))
        else:
            sql = """
                INSERT INTO adoptions (dog_id, adopter_id, adoption_date, returned)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(sql, (self.dog_id, self.adopter_id, self.adoption_date, self.returned))
            self.id = cursor.lastrowid
        conn.commit()

    @classmethod
    def create(cls, dog_id, adopter_id, adoption_date, returned):
        adoption = cls(dog_id, adopter_id, adoption_date, returned)
        adoption.save()
        return adoption

    @classmethod
    def find_by_id(cls, adoption_id):
        sql = "SELECT * FROM adoptions WHERE id = ?"
        cursor.execute(sql, (adoption_id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    def delete(self):
        if self.id is not None:
            sql = "DELETE FROM adoptions WHERE id=?"
            cursor.execute(sql, (self.id,))
            conn.commit()

    @classmethod
    def select_adoptions(cls):
        sql = "SELECT * FROM adoptions"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]
