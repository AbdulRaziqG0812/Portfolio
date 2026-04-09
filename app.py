from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="raziq12@",
        database="portfolio"
    )

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():

    name = request.form['name']
    email = request.form['email']
    contact = request.form['contact']
    message = request.form['message']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO contact_messages (name,email,contact,message)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(query,(name,email,contact,message))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)