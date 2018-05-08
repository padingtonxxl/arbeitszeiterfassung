import sqlite3


class Runtime:

    def __init__(self, path):
        self._path = path
        self._db_path = self._path + '/db/arbeitszeit.db'
        self._db_connection = sqlite3.connect(self._db_path)

    def init(self):
        cursor = self._db_connection.cursor()
        cursor.execute(
            '''CREATE TABLE tageseintraege 
            (user integer, datum integer, von integer, bis integer, stunden real, pause real, soll_differenz real)'''
        )
        self._db_connection.commit()

    def close(self):
        self._db_connection.close()