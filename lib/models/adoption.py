from .config import conn, cursor

class Adoption:
    def __init__(self, dog_id, adopter_id, adoption_date, returned=False, id=None):
        self.id = id
        self.dog_id = dog_id
        self.adopter_id = adopter_id
        self.adoption_date = adoption_date
        self.returned = returned

    def __repr__(self):
        return f"<Adoption {self.dog_id} {self.adopter_id} {self.adoption_date} {self.returned}>"
    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS adoptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dog_id INTEGER NOT NULL,
            adopter_id INTEGER NOT NULL,
            adoption_date DATETIME NOT NULL,
            returned BOOLEAN NOT NULL DEFAULT 0,
            FOREIGN KEY (dog_id) REFERENCES dogs(id),
            FOREIGN KEY (adopter_id) REFERENCES adopters(id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Adoption table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS adoptions;"
        cursor.execute(sql)
        conn.commit()
        print("Adoption table dropped successfully")




    def save(self):
        sql = """
            INSERT INTO adoptions (dog_id, adopter_id, adoption_date, returned)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.dog_id, self.adopter_id, self.adoption_date, self.returned))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, dog_id, adopter_id, adoption_date, returned=False):
        adoption = cls(dog_id, adopter_id, adoption_date, returned)
        adoption.save()
        return adoption

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM adoptions WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None
