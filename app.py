from flask import Flask, request, jsonify
import sqlite3
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/get_customers_sales_2021_2022')
@cross_origin()
def get_customers():
    searchby = request.args.get('searchby')
    search = request.args.get('search')
    orderby = request.args.get('orderby')
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM customers_sales_2021_2022 WHERE "{searchby}" LIKE "{search}%" ORDER BY "first_name" {orderby}')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)