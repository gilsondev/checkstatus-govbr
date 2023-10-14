import argparse

import sentry_sdk
from cancelled_domains import update_domains as update_cancelled_domains
from ping import ping_domains
from sentry_sdk import set_tag

from lib.python.database import create_connection
from lib.python.database import create_cursor

sentry_sdk.init(
    dsn="https://011f53de8eea0a53cb44e163d0453eb5@o4506032925900800.ingest.sentry.io/4506032926031872",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)
set_tag("app", "Checkstatus Scheduler")

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
