import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

def read_config(file_path):
    config_data = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    config_data[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while reading the configuration file: {e}")
    return config_data

def save_to_database(data, db_file):
    try:
        with open(db_file, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving to the database: {e}")

def load_from_database(db_file):
    try:
        with open(db_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Database file '{db_file}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred while loading from the database: {e}")
        return {}

@app.route('/get_config', methods=['GET'])
def get_config():
    config_data = load_from_database('database.json')
    return jsonify(config_data)

if __name__ == "__main__":
    config_file = 'config.txt'
    db_file = 'database.json'
    
    config_data = read_config(config_file)
    save_to_database(config_data, db_file)

    app.run(host='0.0.0.0', port=5000)
