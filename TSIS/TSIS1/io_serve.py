import json
import csv
import os
from connect import connect, parse_date 
from phonebook import get_group_id

conn = connect()
cursor = conn.cursor()

def get_or_create_group(group_name):
    """Находит ID группы или создает новую, если её нет."""
    if not group_name:
        return None
    cursor.execute("SELECT id FROM groups WHERE name ILIKE %s", (group_name,))
    res = cursor.fetchone()
    if res:
        return res[0]
    else:
        cursor.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (group_name,))
        return cursor.fetchone()[0]

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
            "name": c[1],
            "email": c[2],
            "birthday": str(c[3]) if c[3] else None,
            "group": c[4],
            "phones": [{"number": p[0], "type": p[1]} for p in phones]
        })

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    print(f"--- Экспорт завершен: {filename} ---")

def import_from_json(filename="TSIS/TSIS1/contacts.json"):
    """Импорт из JSON с логикой пропуска или перезаписи (Требование 3.3)"""
    if not os.path.exists(filename):
        print("Файл JSON не найден.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        name = item.get('name')
        email = item.get('email')
        birthday = item.get('birthday')
        group_name = item.get('group')
        phones = item.get('phones', [])

        # Проверка на дубликат по имени
        cursor.execute("SELECT id FROM contacts WHERE name = %s", (name,))
        existing = cursor.fetchone()

        if existing:
            choice = input(f"Контакт '{name}' уже существует. Перезаписать (o) или пропустить (s)? ").lower()
            if choice == 's':
                continue
            else:
                # Удаляем старые данные, чтобы записать новые
                cursor.execute("DELETE FROM contacts WHERE id = %s", (existing[0],))

        # Создаем контакт
        group_id = get_or_create_group(group_name)
        cursor.execute(
            "INSERT INTO contacts (name, email, birthday, group_id) VALUES (%s, %s, %s, %s) RETURNING id",
            (name, email, birthday, group_id)
        )
        new_id = cursor.fetchone()[0]

        for p in phones:
            cursor.execute(
                "INSERT INTO phones (contact_id, number, type) VALUES (%s, %s, %s)",
                (new_id, p['number'], p['type'])
            )
    
    conn.commit()
    print("--- Импорт из JSON завершен ---")

def reading_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            name = row.get('name', '').strip()
            phone = row.get('phone', '').strip() # В CSV колонка 'phone'
            if not name or not phone: continue

            phone_type = row.get('type', 'mobile').strip().lower()
            email = row.get('email', '').strip() or None
            birthday = parse_date(row.get('birthday', '').strip())
            group_id = get_or_create_group(row.get('group', '').strip())

            cursor.execute("SAVEPOINT sp")
            try:
                # Ищем существующий контакт
                cursor.execute("SELECT id FROM contacts WHERE name = %s", (name,))
                existing = cursor.fetchone()

                if existing:
                    contact_id = existing[0]
                else:
                    cursor.execute(
                        "INSERT INTO contacts (name, email, birthday, group_id) VALUES (%s, %s, %s, %s) RETURNING id",
                        (name, email, birthday, group_id)
                    )
                    contact_id = cursor.fetchone()[0]

                # Вставляем в таблицу phones (столбец 'number' по твоей схеме)
                cursor.execute(
                    "INSERT INTO phones (contact_id, number, type) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                    (contact_id, phone, phone_type)
                )
                count += 1
            except Exception as e:
                cursor.execute("ROLLBACK TO SAVEPOINT sp")
                print(f"Ошибка в строке {name}: {e}")
        
        conn.commit()
        print(f"--- Успешно обработано из CSV: {count} ---")

if __name__ == "__main__":
    # 1. Сначала пробуем импорт из CSV
    csv_path = "C:/Users/suanb/Desktop/pp2/TSIS/TSIS1/contacts.csv"
    if os.path.exists(csv_path):
        reading_csv(csv_path)
    
    # 2. Делаем экспорт, чтобы создать JSON файл
    export_to_json()

    # 3. Пример запуска импорта из JSON (раскомментируй для теста)
    # import_from_json()

    cursor.close()
    conn.close()