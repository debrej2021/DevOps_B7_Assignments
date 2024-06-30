import os
import json
import mysql.connector
from flask import Flask, jsonify, request

# Define the Flask app
app = Flask(__name__)

# MySQL database connection configuration
db_config = {
    'user': 'root',
    'password': 'root123',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'new_db'
}

# Function to read the configuration file
def read_config_file(file_path):
    config = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    config[key] = value
    except FileNotFoundError:
        print(f"Error: The configuration file {file_path} was not found.")
    except Exception as e:
        print(f"Error reading the configuration file: {e}")
    return config

# Function to save the configuration data to the MySQL database
def save_to_database(data):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS config 
                          (id INT AUTO_INCREMENT PRIMARY KEY, data JSON)''')
        cursor.execute("INSERT INTO config (data) VALUES (%s)", (json.dumps(data),))
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print(f"Error saving to the database: {e}")

# Function to fetch the configuration data from the MySQL database
def fetch_from_database():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT data FROM config ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return json.loads(row[0])
        else:
            return {}
    except mysql.connector.Error as e:
        print(f"Error fetching from the database: {e}")
        return {}

# Define the route to fetch the configuration data
@app.route('/get_config', methods=['GET'])
def get_config():
    data = fetch_from_database()
    return jsonify(data)

# Main function to execute the script
if __name__ == "__main__":
    config_file_path = 'config.txt'
    config_data = read_config_file(config_file_path)
    if config_data:
        save_to_database(config_data)
    app.run(host='0.0.0.0', port=5000)
