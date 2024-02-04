import streamlit as st
import sqlite3

# Adatbázis kapcsolódás létrehozása
conn = sqlite3.connect('userdata.db')
c = conn.cursor()

# Tábla létrehozása, ha még nem létezik
c.execute('''
          CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              gender TEXT
          )
          ''')
conn.commit()

def add_user_to_database(name, gender):
    # Felhasználó hozzáadása az adatbázishoz
    c.execute("INSERT INTO users (name, gender) VALUES (?, ?)", (name, gender))
    conn.commit()

def fetch_all_users():
    # Összes felhasználó lekérdezése az adatbázisból
    c.execute("SELECT * FROM users")
    return c.fetchall()

# Streamlit alkalmazás
def main():
    st.title("Felhasználókezelő Streamlit alkalmazás")

    # Felhasználótól név és nem bekérdezése
    name = st.text_input("Kérlek, add meg a neved:")
    gender = st.radio("Válaszd ki a nemedet:", ("Férfi", "Nő", "Egyéb"))

    # Gomb, amivel hozzáadod az adatbázishoz a felhasználót
    if st.button("Felhasználó hozzáadása"):
        add_user_to_database(name, gender)
        st.success(f"{name} felhasználó hozzáadva az adatbázishoz!")

    # Táblázat létrehozása az összes felhasználó adataival
    users = fetch_all_users()
    st.table(users)

if __name__ == "__main__":
    main()
