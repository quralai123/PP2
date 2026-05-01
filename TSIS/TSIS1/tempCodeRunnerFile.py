from connect import connect

conn = connect()
cursor = conn.cursor()


# TEST PROCEDURES
def test_add_phone():
    cursor.execute("""
        CALL add_phone('Alice Johnson', '+77070000001', 'mobile');
    """)
    conn.commit()
    print("add_phone executed")


def test_move_group():
    cursor.execute("""
        CALL move_to_group('Alice Johnson', 'NewGroup');
    """)
    conn.commit()
    print("move_to_group executed")


# TEST FUNCTION
def test_search():
    cursor.callproc("search_contacts", ["Alice"])

    rows = cursor.fetchall()

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