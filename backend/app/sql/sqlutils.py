# Note: the module name is psycopg, not psycopg3
import psycopg


class SqlExecuter:
    def __init__(self, postgres_url: str) -> None:
        self.postgres_url = postgres_url

    def insert(self, sql: str):
        # Connect to an existing database
        with psycopg.connect(f"{self.postgres_url}") as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:

                # Execute a command
                cur.execute(sql)

                # Make the changes to the database persistent
                conn.commit()
