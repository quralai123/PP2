import psycopg2
from config import host, user, password, db_name
import psycopg2
from config import host, user, password, db_name

def get_connection():
    return psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port="5433"
    )



class DBManager:
    def save_result(self, username, score, level):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                # 1. Находим или создаем игрока
                cursor.execute(
                    "INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING RETURNING id;",
                    (username,)
                )
                res = cursor.fetchone()
                if res:
                    player_id = res[0]
                else:
                    cursor.execute("SELECT id FROM players WHERE username = %s;", (username,))
                    player_id = cursor.fetchone()[0]

                # 2. Записываем сессию
                cursor.execute(
                    "INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s);",
                    (player_id, score, level)
                )
            conn.commit()
            print(f"[DB] Saved: {username} - {score}")
        except Exception as e:
            print(f"[DB] Error saving: {e}")
        finally:
            conn.close()
    def get_top_10(self):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT p.username, s.score 
                    FROM game_sessions s
                    JOIN players p ON s.player_id = p.id
                    ORDER BY s.score DESC 
                    LIMIT 10;
                """
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            print(f"[DB] Error fetching top 10: {e}")
            return []
        finally:
            conn.close()

    def get_personal_best(self, username):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT MAX(s.score) 
                    FROM game_sessions s
                    JOIN players p ON s.player_id = p.id
                    WHERE p.username = %s;
                """
                cursor.execute(query, (username,))
                res = cursor.fetchone()
                return res[0] if res and res[0] is not None else 0
        except Exception as e:
            print(f"[DB] Error fetching personal best: {e}")
            return 0
        finally:
            conn.close()