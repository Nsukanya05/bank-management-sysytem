from flask import Flask, render_template, request
from config import get_db_connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/customers')
def customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, name, balance FROM customers")
    customers_data = cursor.fetchall()
    conn.close()
    return render_template('customers.html', customers=customers_data)

