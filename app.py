from flask import Flask, render_template, jsonify
<<<<<<< HEAD

app = Flask(__name__)

# VA Medical Center
va_medical_center = [
    {
      "name": "Spark M. Matsunaga VA Medical Center",
      "address": "459 Patterson Road, Honolulu, HI 96819-1522",
      "phone": "800-214-1306",
      "mental_health_phone": "800-214-1306",
      "va_health_connect": "833-983-0487",
      "map_link": "https://www.google.com/maps?q=459+Patterson+Road,+Honolulu,+HI+96819-1522",
      "image": "/static/images/va-medicalcenter.jpg"
    }
]

# Outpatient Clinics
outpatient_clinics = [
    {
      "name": "Maui VA Outpatient Clinic",
      "address": "203 Hoohana St #303, Kahului, HI 96732",
      "phone": "808-242-8557",
      "map_link": "https://maps.app.goo.gl/AnCFVXtE7ZevhaF47",
      "image": "/static/images/maui-outpatient.jpg"
    },
    {
      "name": "Hilo VA Outpatient Clinic",
      "address": "Professional Building, 45 Mohouli St, Hilo, HI 96720",
      "phone": "808-969-3833",
      "map_link": "https://maps.app.goo.gl/2YS7WmWsgohkFq757",
      "image": "/static/images/hilo-outpatient.png"
    },
    {
      "name": "Lihue VA Outpatient Clinic",
      "address": "4473 Pahe'e St, Lihue, HI 96766",
      "phone": "808-246-1163",
      "map_link": "https://www.google.com/maps?q=4485+Pahe'e+Street+Lihue,+HI+96765",
      "image": "/static/images/lihue-outpatient.jpg"
    },
    {
      "name": "Molokai VA Community-Based Outpatient Clinic",
      "address": "123 Example St, Molokai, HI 96748",
      "phone": "808-123-4567",
      "map_link": "https://maps.example.com/molokai",
      "image": "/static/images/molokai-outpatient.jpg"
    },
    {
      "name": "Kona Community-Based Outpatient Clinic",
      "address": "73-4976 Kamanu St, Kailua-Kona, HI 96740",
      "phone": "808-329-0574",
      "map_link": "https://www.google.com/maps?q=73-4976+Kamanu+St,+Kailua-Kona,+HI+96740",
      "image": "/static/images/kona-outpatient.jpg"
    },
    {
      "name": "Leeward Community-Based Outpatient Clinic",
      "address": "91-2139 Fort Weaver Rd, Ewa Beach, HI 96706",
      "phone": "808-458-5084",
      "map_link": "https://www.google.com/maps?q=91-2139+Fort+Weaver+Rd,+Ewa+Beach,+HI+96706",
      "image": "/static/images/ewabeach-outpatient.jpg"
    }
]

# Vet Centers
vet_centers = [
    {
      "name": "Hilo Vet Center",
      "address": "70 Lanihuli Street, Suite 102, Hilo, HI 96720",
      "phone": "808-969-3833",
      "map_link": "https://www.google.com/maps?q=70+Lanihuli+Street+Hilo,+HI+96720",
      "image": "/static/images/hilo-vaclinic.jpg"
    },
    {
      "name": "Honolulu Vet Center",
      "address": "1680 Kapiolani Boulevard, Suite F-3, Honolulu, HI 96814-3700",
      "phone": "808-973-8387",
      "map_link": "https://www.google.com/maps?q=1680+Kapiolani+Boulevard+Honolulu,+HI+96814-3700",
      "image": "/static/images/honolulu-vaclinic.jpg"
    },
    {
      "name": "Maui Vet Center",
      "address": "157 Ma'a Street, Kahului, HI 96732",
      "phone": "808-242-8557",
      "map_link": "https://www.google.com/maps?q=157+Ma'a+Street+Kahului,+HI+96732",
      "image": "/static/images/maui-vaclinic.jpg"
    },
    {
      "name": "Kona Vet Center",
      "address": "73-4976 Kamanu Street, Suite 207, Kailua-Kona, HI 96740",
      "phone": "808-329-0574",
      "map_link": "https://www.google.com/maps?q=73-4976+Kamanu+Street+Kailua-Kona,+HI+96740",
      "image": "/static/images/kona-vaclinic.jpg"
    },
    {
      "name": "West Oahu Vet Center",
      "address": "91-1051 Franklin D. Roosevelt Avenue, Kapolei, HI 96707",
      "phone": "808-458-5084",
      "map_link": "https://www.google.com/maps?q=91-1051+Franklin+D.+Roosevelt+Avenue+Kapolei,+HI+96707",
      "image": "/static/images/west-oahu-vaclinics.jpg"
    }
]

# ROUTES

@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/api/medical-center', methods=['GET'])
def get_medical_center():
    return jsonify(va_medical_center)

@app.route('/api/outpatient-clinics', methods=['GET'])
def get_outpatient_clinics():
    return jsonify(outpatient_clinics)

@app.route('/api/vet-centers', methods=['GET'])
def get_vet_centers():
    return jsonify(vet_centers)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
=======
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
>>>>>>> 179321ab455c936578c63875c26cb03b74cc9c5c
