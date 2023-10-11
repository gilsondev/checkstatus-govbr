import argparse

from cancelled_domains import update_domains as update_cancelled_domains
from ping import ping_domains

from lib.database import create_connection
from lib.database import create_cursor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Executes tasks for checkstatus-govbr")
    parser.add_argument(
        "task", choices=["ping", "update_cancelled_domains"], help="Task to be executed"
    )
    args = parser.parse_args()

    conn = create_connection()
    cursor = create_cursor(conn)

    if args.task == "ping":
        ping_domains(cursor)
    elif args.task == "update_cancelled_domains":
        update_cancelled_domains(cursor)

    conn.commit()
    conn.close()
    cursor.close()
