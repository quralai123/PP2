from connect import connect

conn = connect()
cursor = conn.cursor()

def test_add_phone():
    name = input("Имя контакта: ")
    phone = input("Номер телефона: ")
    p_type = input("Тип (home/work/mobile): ")
    
    cursor.execute("CALL add_phone(%s, %s, %s);", (name, phone, p_type))
    conn.commit()
    print(f"Запрос на добавление {phone} для {name} отправлен!")

def test_move_group():
    name = input("Имя контакта: ")
    group = input("Новая группа: ")
    
    cursor.execute("CALL move_to_group(%s, %s);", (name, group))
    conn.commit()
    print(f"Запрос на перенос {name} в {group} отправлен!")

def test_search():
    query = input("Введите текст для поиска: ")
    cursor.execute("SELECT * FROM search_contacts(%s);", (query,))
    rows = cursor.fetchall()

    if not rows:
        print("Ничего не найдено!")
    for r in rows:
        print(r)


while True:
    print("""
1. add_phone
2. move_to_group
3. search_contacts
4. exit
""")

    choice = input("> ")

    if choice == "1":
        test_add_phone()

    elif choice == "2":
        test_move_group()

    elif choice == "3":
        test_search()

    elif choice == "4":
        break


cursor.close()
conn.close()