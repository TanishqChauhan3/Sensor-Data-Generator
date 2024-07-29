import json
import random
import time

def data():
    data = {
        "temperature": random.uniform(-10, 40),  
        "humidity": random.uniform(0, 100)       
    }
    return data

def save_to_json(data, filename='sensor_data.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    while True:
        sensor_data = data()
        save_to_json(sensor_data)
        print("Generated and saved data:", sensor_data)
        time.sleep(5) 
