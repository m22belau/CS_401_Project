# CS_401_Project

# Hawaii Veterans Resource Directory

## Purpose

Hawaii has a significant veteran population; however, many veterans face challenges as they are often overlooked and underserved. With a wide range of ages—many being older; adjusting to the constantly changing real and digital world can be difficult. Key issues veterans face include geographical barriers, limited healthcare access, financial struggles, mental health challenges, and employment difficulties.
Our goal is to create a web-based resource hub for veterans in Hawaii. This platform will be clear, user-friendly, and centralized, providing essential information on VA services, benefits, and community programs. Through this website, veterans will be able to find VA healthcare facilities, better understand their benefits, and access job and housing resources. Ultimately, we aim to simplify the process of connecting veterans with the support they need and deserve

Veterans and their families can:
- Find nearby VA medical resources
- View contact information and addresses
- Access direct links to Google Maps for each facility

All data is provided in JSON format and served through a simple API.

---

## Technologies Used 2. Run it Locally

- **Flask** (Python web framework)
- **HTML/CSS/JavaScript** (Single-page layout)
- **Bootstrap** (for responsive design)
- **JSON API** (data-driven dynamic loading)
- **Docker** (to simplify local deployment)

---

## Getting Started

### 1. Clone the Repository
In terminal:

git clone https://github.com/your-username/hawaii-veterans-resources.git
cd hawaii-veterans-resources

### 2. Run it Locally
Install dependencies:
pip install -r requirements.txt

Start the server:
python app.py

## Running it with Docker
### 1. Build the Image

docker build -t hawaii-vet-site .

### 2. Run the Container
docker run -p 5002:5000 hawaii-vet-site



