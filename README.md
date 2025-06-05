 ****Real_Time_Location_Tracker****  

---

**Real-Time Location Tracking Web App (Using Flask & OpenStreetMap)**  

**Overview**  
This project is a **real-time location tracking web app** that allows users to share their **current location** on a map when they click a button. The app is built using:  
1. **Flask (Python)** – Handles the backend & stores user location  
2. **Leaflet.js + OpenStreetMap** – Displays a live map without requiring a paid API  
3. **JavaScript (Geolocation API)** – Gets the user's real-time GPS location  
4. **HTML & CSS** – Provides a simple UI for users  

The project **does not require Google Maps API**, making it **100% free** to use.  

---

**Project Structure**  

```
/Real-Time-Location-Tracking
│── /templates
│   ├── index.html          # Frontend: Displays the map and "Track Me" button
│── app.py                  # Backend: Flask server to receive and store location
│── requirements.txt        # List of required dependencies
│── README.md               # Project documentation (this file)
```

---

**Features**  
=> **Get user’s real-time GPS location**  
=> **Display the live location on a map**  
=> **Uses OpenStreetMap (Free alternative to Google Maps)**  
=> **Built with Flask and JavaScript**  
=> **Simple, lightweight, and fast**  

---

**How It Works**  

1.**User clicks the "Track Me" button**  
2️. **Browser asks for location permission**  
3️. **JavaScript captures the latitude & longitude**  
4️. **Location is sent to the Flask backend**  
5️. **Backend stores the location** and sends it back to update the map  
6️. **Leaflet.js displays the location on an interactive map**  

---

**Installation & Setup**  

**1️. Install Dependencies**  
Make sure Python is installed, then run:  

```bash
pip install flask
```

**2️. Run the Flask Server**  
```cmd
python app.py
```

**3️. Open in Browser**  
Go to:  
```
http://127.0.0.1:5000/
```
Click **"Track Me"** to see your real-time location on the map!  

---

**Code Breakdown**  

**1. Frontend (`index.html`)**  
This file:  
--> Contains a **"Track Me"** button  
--> Uses **JavaScript** to get user location  
--> Sends the location to the Flask server  
--> Uses **Leaflet.js + OpenStreetMap** to display the map  

**2. Backend (`app.py`)**  
This file:  
--> Uses **Flask** to handle HTTP requests  
--> Stores the **latest user location**  
--> Sends back the stored location to update the map  

---

**Technologies Used**  

| Technology              | Purpose                             |
|-------------------------|-------------------------------------|
| **Flask**               | Backend (Handles requests)          |
| **JavaScript**          | Gets location using Geolocation API |
| **Leaflet.js**          | Displays map using OpenStreetMap    |
| **OpenStreetMap (OSM)** | Free alternative to Google Maps     |
| **HTML & CSS**          | Simple UI for users                 |

---

**Future Enhancements**  
--> Track **multiple users** and display them on the same map  
--> Store location history in a **database**  
--> Add **real-time movement tracking**  
--> Improve UI with better design  

---

**Contributions**  
Feel free to contribute by:  
==> Adding new features  
==> Fixing bugs  
==> Improving UI  
