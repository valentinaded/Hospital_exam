import sqlite3
import streamlit as st

# Create a SQLite database named 'hospital'
conn = sqlite3.connect('hospital.db')
c = conn.cursor()

# Create the 'patients' table with a foreign key reference to the 'doctors' table
c.execute('''
          CREATE TABLE IF NOT EXISTS patients (
              id INTEGER PRIMARY KEY,
              name TEXT,
              birthday TEXT,
              phone_number TEXT,
              type_of_visit TEXT
          )
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS doctors (
              id INTEGER PRIMARY KEY,
              name TEXT,
              phone_number TEXT,
              specialism TEXT
          )
          ''')

# Define CRUD operations for the 'patients' table
def create_patient(name, birthday, phone_number, type_of_visit):
    c.execute("INSERT INTO patients (name, birthday, phone_number, type_of_visit) VALUES (?, ?, ?, ?)",
              (name, birthday, phone_number, type_of_visit))
    conn.commit()

def read_patient(name):
    c.execute("SELECT * FROM patients WHERE name=?", (name,))
    return c.fetchall()

def update_patient(name, birthday, phone_number, type_of_visit):
    c.execute("UPDATE patients SET birthday=?, phone_number=?, type_of_visit=? WHERE name=?",
              (birthday, phone_number, type_of_visit, name))
    conn.commit()

def delete_patient(name):
    c.execute("DELETE FROM patients WHERE name=?", (name,))
    conn.commit()

# Define CRUD operations for the 'doctors' table
def create_doctor(name, phone_number, specialism):
    c.execute("INSERT INTO doctors (name, phone_number, specialism) VALUES (?, ?, ?)",
              (name, phone_number, specialism))
    conn.commit()

def read_doctor(name):
    c.execute("SELECT * FROM doctors WHERE name=?", (name,))
    return c.fetchall()

def update_doctor(name, phone_number, specialism):
    c.execute("UPDATE doctors SET phone_number=?, specialism=? WHERE name=?",
              (phone_number, specialism, name))
    conn.commit()

def delete_doctor(name):
    c.execute("DELETE FROM doctors WHERE name=?", (name,))
    conn.commit()

# Define the Streamlit app
def app():
    st.title('Hospital Database')
    menu = ['Home', 'Patient', 'Doctor']
    choice = st.sidebar.selectbox('Select an option', menu)
    
    if choice == 'Home':
        st.subheader('Home')
        st.write('Welcome to the Hospital Database! Use the sidebar to navigate to the patient or doctor section.')
    
    elif choice == 'Patient':
        st.subheader('Patient')
        st.write('Add a new patient')
        name = st.text_input('Name', key='name_input')
        birthday = st.date_input('Birthday', key='birthday_input')
        phone_number = st.text_input('Phone Number', key='phone_input')
        type_of_visit = st.text_input('Type of Visit', key='visit_input')
        if st.button('Create'):
            create_patient(name, birthday, phone_number, type_of_visit)
            st.success('Patient added!')
        
        st.write('Search for a patient')
        name = st.text_input('Name', key='search_name_input')
        if st.button('Search'):
            result = read_patient(name)
            if len(result) > 0:
                st.write(result)
            else:
                st.warning('Patient not found')
        
        st.write('Update a patient')
        name = st.text_input('Name', key='update_name_input')
        birthday = st.date_input('Birthday', key='update_birthday_input')
        phone_number = st.text_input('Phone Number', key='update_phone_input')
        type_of_visit = st.text_input('Type of Visit', key='update_visit_input')
        if st.button('Update'):
            update_patient(name, birthday, phone_number, type_of_visit)
            st.success('Patient updated!')
        
        st.write('Delete a patient')
        name = st.text_input('Name', key='delete_name_input')
        if st.button('Delete'):
            delete_patient(name)
            st.success('Patient deleted!')
    elif choice == 'Doctor':
        st.subheader('Doctor')
        st.write('Add a new doctor')
        name = st.text_input('Name', key='doc_name_input')
        phone_number = st.text_input('Phone Number', key='doc_phone_input')
        specialism = st.text_input('Specialism', key='doc_specialism_input')
        if st.button('Create'):
            create_doctor(name, phone_number, specialism)
            st.success('Doctor added!')
        
        st.write('Search for a Doctor')
        name = st.text_input('Name', key='search_name_input')
        if st.button('Search'):
            result = read_patient(name)
            if len(result) > 0:
                st.write(result)
            else:
                st.warning('Doctor not found')
        
        st.write('Update a doctor')
        name = st.text_input('Name', key='doc_update_name_input')
        phone_number = st.text_input('Phone Number', key='doc_update_phone_input')
        specialism = st.text_input('Specialism', key='doc_update_specialism_input')
        if st.button('Update'):
            update_doctor(name, phone_number, specialism)
            st.success('Doctor updated!')
        
        st.write('Delete a doctor')
        name = st.text_input('Name', key='doc_delete_name_input')
        if st.button('Delete'):
            delete_doctor(name)
            st.success('Doctor deleted!')
app()