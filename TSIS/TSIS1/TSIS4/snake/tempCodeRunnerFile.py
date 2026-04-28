import psycopg2
from config import host, user, password, db_name

connection = None
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port="5433"
    )
    connection.autocommit = True
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(f"Server version: {cursor.fetchone()}")

    # Создаем таблицу
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE players (
                id       SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL
            );

            CREATE TABLE game_sessions (
                id            SERIAL PRIMARY KEY,
                player_id     INTEGER REFERENCES players(id),
                score         INTEGER   NOT NULL,
                level_reached INTEGER   NOT NULL,
                played_at     TIMESTAMP DEFAULT NOW()
            );"""
        )
        print("[INFO] Table 'TSIS4' created successfully")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL:", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")