
import sqlite3
import os.path


HOST_NAME = 'localhost'
HOST_PORT = '7777'


def search(descriptor, database):
    """
    Searches for all room IDs whose name contains the descriptor.

    :param descriptor: any string that shall be searched for
    :param database: path to the SQLITE database file
    :return: list of row IDs as strings
    """
    if not os.path.exists(database):
        raise OSError('Database file does not exist at {}'.format(database))

    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    return [row for row in cursor.execute("SELECT room_id IN Rooms WHERE room_name=?", descriptor)]
