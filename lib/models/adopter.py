from .config import conn, cursor

class Adopter:
    def __init__(self, name, contact, id=None):
        self.id = id
        self.name = name
        self.contact = contact

    def __repr__(self):
        return f"<Adopter {self.name} {self.contact}>"


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
        sql = "DROP TABLE IF EXISTS adopters;"
        cursor.execute(sql)
        conn.commit()
        print("Adopter table dropped successfully")

    def save(self):
        sql = """
            INSERT INTO adopters (name, contact)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.name, self.contact))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, contact):
        adopter = cls(name, contact)
        adopter.save()
        return adopter

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM adopters WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None