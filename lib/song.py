from config import CONN, CURSOR


# class Song:

#     def __init__(self, name, album):
#         self.id = None
#         self.name = name
#         self.album = album

#     @classmethod
#     def create_table(self):
#         sql = """
#             CREATE TABLE IF NOT EXISTS songs (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT,
#                 album TEXT
#             )
#         """

#         CURSOR.execute(sql)

#     def save(self):
#         sql = """
#             INSERT INTO songs (name, album)
#             VALUES (?, ?)
#         """

#         CURSOR.execute(sql, (self.name, self.album))
#     @classmethod
#     def create(cls, name, album):
#         song = Song(name, album)
#         song.save()
#         return song
    

# song = Song.create("Hello", "25")
# song.name
# # => "Hello"
# song.album
# # => "25"

import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

class Song:

    all = []

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS songs
        """

        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song