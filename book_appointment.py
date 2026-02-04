import sqlite3

# Connect to database (creates it if not exists)
conn = sqlite3.connect("clinic.db")
cursor = conn.cursor()

# Create appointment table
cursor.execute("""
CREATE TABLE IF NOT EXISTS appointment (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    appointment_date TEXT,
    appointment_time TEXT
)
""")

# Sample appointment data
patient_id = 1
doctor_id = 2
appointment_date = "2025-01-10"
appointment_time = "10:00"

# Insert appointment
cursor.execute("""
INSERT INTO appointment (patient_id, doctor_id, appointment_date, appointment_time)
VALUES (?, ?, ?, ?)
""", (patient_id, doctor_id, appointment_date, appointment_time))

conn.commit()
conn.close()

print("Appointment booked successfully")
