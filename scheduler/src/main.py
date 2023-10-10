from ping import ping_domains

from lib.database import create_connection
from lib.database import create_cursor

if __name__ == "__main__":
    conn = create_connection()
    cursor = create_cursor(conn)

    ping_domains(cursor)

    conn.commit()
    conn.close()
    cursor.close()
