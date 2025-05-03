from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Directory where JSON files are located
DATA_DIR = os.path.join(os.path.dirname(__file__), 'backend')

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/medical_center')
def get_medical_center():
    with open(os.path.join(DATA_DIR, 'medical_center.json')) as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/outpatient')
def get_outpatient():
    with open(os.path.join(DATA_DIR, 'outpatient.json')) as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/vet_centers')
def get_vet_centers():
    with open(os.path.join(DATA_DIR, 'vet_centers.json')) as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
