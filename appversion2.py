from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to connect to the database and fetch beneficiaries
def get_beneficiaries():
    conn = sqlite3.connect('beneficiaries.db')  # Connect to your database
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, age, gender, phone_number, state, address, photo FROM beneficiaries")
    beneficiaries = cursor.fetchall()
    
    conn.close()
    
    # Convert to a list of dictionaries for easier access in the HTML template
    beneficiaries_data = []
    for row in beneficiaries:
        beneficiaries_data.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "gender": row[3],
            "phone_number": row[4],
            "state": row[5],
            "address": row[6],
            "photo": row[7]  # Assuming the photo field stores the file path
        })
    
    return beneficiaries_data

@app.route('/beneficiaries')
def beneficiaries_page():
    beneficiaries = get_beneficiaries()  # Fetch beneficiaries from the database
    return render_template('Beneficiary.html', beneficiaries=beneficiaries)

if __name__ == "__main__":
    app.run(debug=True)
