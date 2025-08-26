# 🌱 Smart Crop Recommendation System

A **web-based application** that predicts the most suitable crop for cultivation based on soil nutrients, climate conditions, and rainfall. Built using **Flask**, **Python**, and a **Machine Learning model**, this system provides crop recommendations along with useful tips for optimal growth.  

---

## 🚀 Features

- Predicts crops based on **N, P, K values**, temperature, humidity, pH, and rainfall.  
- Validates inputs to ensure **realistic crop conditions**.  
- Displays **dynamic bubble animation** for a modern UI.  
- Provides **crop-specific tips** for better farming decisions.  
- Fully **responsive design** for desktop and mobile devices.  

---

## ⚙️ Technologies Used

- **Python 3.10+**  
- **Flask** – Web framework  
- **scikit-learn** – For ML model prediction  
- **HTML, CSS, JavaScript** – Frontend  
- **Bootstrap** – Responsive UI  
- **Pickle** – Saving and loading ML models  

---

## 📝 Usage

Enter the following inputs on the home page:

- Nitrogen (N)  
- Phosphorus (P)  
- Potassium (K)  
- Temperature (°C)  
- Humidity (%)  
- Soil pH  
- Rainfall (mm)  

Steps:

1. Click **Analyse**.  
2. View the recommended crop and tips.  
3. Click **⬅️ Try Again** to make another prediction.  

---

## ⚠️ Input Validation Rules

- N, P, K values **cannot be negative**.  
- Rainfall must be between **20 – 400 mm**.  
- Temperature must be between **10 – 45°C**.  
- Humidity must be between **20 – 95%**.  
- Soil pH must be between **4.5 – 9.0**.  

Invalid inputs trigger a **flash alert**.

---

## 🌾 Crop Tips

- Rice: Needs heavy rainfall & humid conditions.  
- Maize: Grows well in warm climate with moderate rainfall.  
- Chickpea: Requires dry climate, avoid excess water.  
- Kidneybeans: Prefers moderate rainfall & loamy soil.  
- Pigeonpeas: Needs long warm season with low humidity.  
- Mothbeans: Grows best in arid and semi-arid regions.  
- Mungbean: Short duration crop, prefers warm humid climate.  
- Blackgram: Needs warm weather with moderate rains.  
- Lentil: Prefers cool climate, well-drained soil.  
- Pomegranate: Grows in hot dry climate with low water.  
- Banana: High humidity, requires rich loamy soil.  
- Mango: Needs tropical climate with hot summers.  
- Grapes: Requires dry warm summers, deep soil.  
- Watermelon: Hot climate with sandy soil works best.  
- Muskmelon: Grows in warm and dry climate.  
- Apple: Requires cold climate, hilly areas.  
- Orange: Subtropical climate, requires well-drained soil.  
- Papaya: Needs tropical climate with good rainfall.  
- Coconut: Hot & humid coastal regions best.  
- Cotton: Black soil & warm climate with low humidity.  
- Jute: Requires warm humid climate & alluvial soil.  
- Coffee: Prefers cool shade & well-drained soil.

---

## 📂 Folder Structure
smart-crop-recommendation/
│
├── app.py
├── model.pkl
├── minmaxscaler.pkl
├── standscaler.pkl
├── requirements.txt
├── templates/
│ ├── index.html
│ └── result.html
└── static/
├── style.css
├── bg.jpg
├── home.png
├── result.png
└── error.png
---

## 💡 Future Enhancements

- Add **location-based weather API integration** for dynamic temperature and rainfall.  
- Improve **ML model** with more crop types and updated datasets.  
- Add **multi-language support** for farmers.  
- Enable **downloadable crop reports**.
