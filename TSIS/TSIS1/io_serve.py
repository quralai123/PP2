import json
import csv
import os
from connect import connect, parse_date 
from phonebook import get_group_id

conn = connect()
if conn:
    cursor = conn.cursor()
else:
    print("Не удалось подключиться к базе данных. connect.py")
    exit()

def export_to_json(filename="TSIS/TSIS1/contacts.json"):
    cursor.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
    """)
    contacts = cursor.fetchall()
    result = []

    for c in contacts:
        contact_id = c[0]
        cursor.execute("SELECT number, type FROM phones WHERE contact_id = %s", (contact_id,))
        phones = cursor.fetchall()

        result.append({
            "id": contact_id,
            "name": c[1],
            "email": c[2],
            "birthday": str(c[3]) if c[3] else None,
            "group": c[4],
            "phones": [{"number": p[0], "type": p[1]} for p in phones]
        })

    # Создаем папку, если её нет
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    print(f"Данные экспортированы в {filename}")

def reading_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            name = row.get('name', '').strip()
            phone = row.get('phone', '').strip()

            if not name or not phone:
                continue

            phone_type = row.get('type', 'mobile').strip().lower()
            if phone_type not in ("home", "work", "mobile"):
                phone_type = "mobile"

            email = row.get('email', '').strip() or None
            birthday = parse_date(row.get('birthday', '').strip())
            group_name = row.get('group', '').strip()
            group_id = get_group_id(group_name)

            cursor.execute("SAVEPOINT sp")
            try:
                cursor.execute(
                    "SELECT id FROM contacts WHERE name = %s AND email IS NOT DISTINCT FROM %s",
                    (name, email)
                )
                existing = cursor.fetchone()

                if existing:
                    contact_id = existing[0]
                else:
                    cursor.execute(
                        "INSERT INTO contacts (name, email, birthday, group_id) "
                        "VALUES (%s, %s, %s, %s) RETURNING id",
                        (name, email, birthday, group_id)
                    )
                    contact_id = cursor.fetchone()[0]

                cursor.execute(
                    "INSERT INTO phones (contact_id, number, type) "
                    "VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                    (contact_id, phone, phone_type)
                )
                count += 1
            except Exception as e:
                cursor.execute("ROLLBACK TO SAVEPOINT sp")
                print(f"Ошибка в строке {row}: {e}")
        
        conn.commit()
        print(f"Успешно обработано строк: {count}")

if __name__ == "__main__":
    csv_path = "C:/Users/suanb/Desktop/pp2/TSIS/TSIS1/contacts.csv"
    
    if os.path.exists(csv_path):
        reading_csv(csv_path)
    else:
        print(f"Файл не найден: {csv_path}")
        export_to_json()

    cursor.close()
    conn.close()