import sqlite3

def init_db():
    conn = sqlite3.connect('cakrawala_helpdesk.db')
    c = conn.cursor()
    # Membuat tabel untuk menyimpan tiket
    c.execute('''CREATE TABLE IF NOT EXISTS tickets 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  user_name TEXT, 
                  complaint TEXT, 
                  priority TEXT, 
                  status TEXT)''')
    conn.commit()
    conn.close()

def save_ticket(name, complaint, priority):
    conn = sqlite3.connect('cakrawala_helpdesk.db')
    c = conn.cursor()
    c.execute("INSERT INTO tickets (user_name, complaint, priority, status) VALUES (?, ?, ?, 'Pending')", 
              (name, complaint, priority))
    conn.commit()
    conn.close()