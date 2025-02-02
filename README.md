 Real_Time_Location_Tracker  

---

**Real-Time Location Tracking Web App (Using Flask & OpenStreetMap)**  

**📌 Overview**  
This project is a **real-time location tracking web app** that allows users to share their **current location** on a map when they click a button. The app is built using:  
✅ **Flask (Python)** – Handles the backend & stores user location  
✅ **Leaflet.js + OpenStreetMap** – Displays a live map without requiring a paid API  
✅ **JavaScript (Geolocation API)** – Gets the user's real-time GPS location  
✅ **HTML & CSS** – Provides a simple UI for users  

The project **does not require Google Maps API**, making it **100% free** to use.  

---

**📂 Project Structure**  

```
/Real-Time-Location-Tracking
│── /templates
│   ├── index.html          # Frontend: Displays the map and "Track Me" button
│── app.py                  # Backend: Flask server to receive and store location
│── requirements.txt        # List of required dependencies
│── README.md               # Project documentation (this file)
```

---

**📌 Features**  
✅ **Get user’s real-time GPS location**  
✅ **Display the live location on a map**  
✅ **Uses OpenStreetMap (Free alternative to Google Maps)**  
✅ **Built with Flask and JavaScript**  
✅ **Simple, lightweight, and fast**  

---

**🚀 How It Works**  

1️⃣ **User clicks the "Track Me" button**  
2️⃣ **Browser asks for location permission**  
3️⃣ **JavaScript captures the latitude & longitude**  
4️⃣ **Location is sent to the Flask backend**  
5️⃣ **Backend stores the location** and sends it back to update the map  
6️⃣ **Leaflet.js displays the location on an interactive map**  

---

**🛠️ Installation & Setup**  

**1️⃣ Install Dependencies**  
Make sure Python is installed, then run:  

```bash
pip install flask
```

**2️⃣ Run the Flask Server**  
```cmd
python app.py
```

**3️⃣ Open in Browser**  
Go to:  
```
http://127.0.0.1:5000/
```
Click **"Track Me"** to see your real-time location on the map!  

---

**📌 Code Breakdown**  

**🔹 1. Frontend (`index.html`)**  
This file:  
✅ Contains a **"Track Me"** button  
✅ Uses **JavaScript** to get user location  
✅ Sends the location to the Flask server  
✅ Uses **Leaflet.js + OpenStreetMap** to display the map  

**🔹 2. Backend (`app.py`)**  
This file:  
✅ Uses **Flask** to handle HTTP requests  
✅ Stores the **latest user location**  
✅ Sends back the stored location to update the map  

---

**🌍 Technologies Used**  

| Technology              | Purpose                             |
|-------------------------|-------------------------------------|
| **Flask**               | Backend (Handles requests)          |
| **JavaScript**          | Gets location using Geolocation API |
| **Leaflet.js**          | Displays map using OpenStreetMap    |
| **OpenStreetMap (OSM)** | Free alternative to Google Maps     |
| **HTML & CSS**          | Simple UI for users                 |

---

**📌 Future Enhancements**  
🔹 Track **multiple users** and display them on the same map  
🔹 Store location history in a **database**  
🔹 Add **real-time movement tracking**  
🔹 Improve UI with better design  

---

**📜 License**  
This project is **open-source** and free to use under the **MIT License**.  

---

**📩 Contributions**  
Feel free to contribute by:  
✅ Adding new features  
✅ Fixing bugs  
✅ Improving UI  
