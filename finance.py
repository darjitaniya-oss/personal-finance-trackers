from database import connect

def add_transaction(t_type, amount):
    conn = connect()
    cur = conn.cursor()

    cur.execute("INSERT INTO transactions (type, amount) VALUES (?, ?)", (t_type, amount))

    conn.commit()
    conn.close()

def view_transactions():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM transactions")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()
