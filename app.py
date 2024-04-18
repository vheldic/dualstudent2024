from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/get_customers_sales_2021_2022')
def get_firstcustomers():
    return get_customers(1)

@app.route('/get_customers_sales_2021_2022/<int:pagination>')
def get_customers(pagination):
    start = 30 * (pagination-1)
    numberItems = 30
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM customers_sales_2021_2022 LIMIT {start},{numberItems}')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)