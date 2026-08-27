import re, sqlite3
from datetime import datetime

con = sqlite3.connect('chama.db')
con.execute('CREATE TABLE IF NOT EXISTS chama (phone TEXT, amount INTEGER, time TEXT)')
con.commit()

def smart_parse(text):
    t = text.lower()
    m_amt = re.search(r'(\d+)(k)?', t.replace(',', ''))
    amt = 0
    if m_amt:
        amt = int(m_amt.group(1))
        if m_amt.group(2) == 'k':
            amt *= 1000
    m_phone = re.search(r'(0)(7|1)\d{8}', text)
    phone = m_phone.group(0) if m_phone else None
    return amt, phone

print("ChamaOS v2.1 ON - Andika: nimelipa 1000 0712000012")

while True:
    msg = input("Andika ujumbe: ").strip()
    if msg.lower() == "exit":
        break
    if "report" in msg.lower():
        rows = con.execute('SELECT phone, SUM(amount) FROM chama GROUP BY phone').fetchall()
        total = 0
        for ph, s in rows:
            print(f"{ph}: {s} KES")
            total += s
        print(f"JUMLA YOTE: {total} KES\n")
        continue
    amt, phone = smart_parse(msg)
    if amt > 0:
        if not phone:
            phone = input("Namba gani? ")
        con.execute('INSERT INTO chama VALUES (?,?,?)', (phone, amt, str(datetime.now())))
        con.commit()
        print(f"Sawa! {phone} -> {amt} KES\n")
    else:
        print("Mfano: nimelipa 1000 0712345678\n")import re, sqlite3
from datetime import datetime

con = sqlite3.connect('chama.db')
con.execute('CREATE TABLE IF NOT EXISTS chama (phone TEXT, amount INTEGER, time TEXT)')
con.commit()

def smart_parse(text):
    t = text.lower()
    m_amt = re.search(r'(\d+)(k)?', t.replace(',', ''))
    amt = 0
    if m_amt:
        amt = int(m_amt.group(1))
        if m_amt.group(2) == 'k':
            amt *= 1000
    m_phone = re.search(r'(0)(7|1)\d{8}', text)
    phone = m_phone.group(0) if m_phone else None
    return amt, phone

print("ChamaOS v2.1 ON - Andika: nimelipa 1000 0712000012")

while True:
    msg = input("Andika ujumbe: ").strip()
    if msg.lower() == "exit":
        break
    if "report" in msg.lower():
        rows = con.execute('SELECT phone, SUM(amount) FROM chama GROUP BY phone').fetchall()
        total = 0
        for ph, s in rows:
            print(f"{ph}: {s} KES")
            total += s
        print(f"JUMLA YOTE: {total} KES\n")
        continue
    amt, phone = smart_parse(msg)
    if amt > 0:
        if not phone:
            phone = input("Namba gani? ")
        con.execute('INSERT INTO chama VALUES (?,?,?)', (phone, amt, str(datetime.now())))
        con.commit()
        print(f"Sawa! {phone} -> {amt} KES\n")
    else:
        print("Mfano: nimelipa 1000 0712345678\n")
