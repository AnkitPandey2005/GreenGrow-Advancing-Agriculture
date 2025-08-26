from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import pickle

app = Flask(__name__)
app.secret_key = "supersecretkey"   # for flashing error messages

# Load model + scalers
model = pickle.load(open("model.pkl", "rb"))
mx = pickle.load(open("minmaxscaler.pkl", "rb"))
sc = pickle.load(open("standscaler.pkl", "rb"))

# Mapping dict
crop_dict = {
 'rice': 1, 'maize': 2, 'chickpea': 3, 'kidneybeans': 4, 'pigeonpeas': 5,
 'mothbeans': 6, 'mungbean': 7, 'blackgram': 8, 'lentil': 9, 'pomegranate': 10,
 'banana': 11, 'mango': 12, 'grapes': 13, 'watermelon': 14, 'muskmelon': 15,
 'apple': 16, 'orange': 17, 'papaya': 18, 'coconut': 19, 'cotton': 20,
 'jute': 21, 'coffee': 22
}
inv_crop_dict = {v: k for k, v in crop_dict.items()}

# Tips dict
tips = {
 "rice": "🌾 Needs heavy rainfall & humid conditions.",
 "maize": "🌽 Grows well in warm climate with moderate rainfall.",
 "chickpea": "🥘 Requires dry climate, avoid excess water.",
 "kidneybeans": "🍛 Prefers moderate rainfall & loamy soil.",
 "pigeonpeas": "🌱 Needs long warm season with low humidity.",
 "mothbeans": "🌿 Grows best in arid and semi-arid regions.",
 "mungbean": "🥗 Short duration crop, prefers warm humid climate.",
 "blackgram": "⚫ Needs warm weather with moderate rains.",
 "lentil": "🥬 Prefers cool climate, well-drained soil.",
 "pomegranate": "🍎 Grows in hot dry climate with low water.",
 "banana": "🍌 High humidity, requires rich loamy soil.",
 "mango": "🥭 Needs tropical climate with hot summers.",
 "grapes": "🍇 Requires dry warm summers, deep soil.",
 "watermelon": "🍉 Hot climate with sandy soil works best.",
 "muskmelon": "🍈 Grows in warm and dry climate.",
 "apple": "🍏 Requires cold climate, hilly areas.",
 "orange": "🍊 Subtropical climate, requires well-drained soil.",
 "papaya": "🥭 Needs tropical climate with good rainfall.",
 "coconut": "🥥 Hot & humid coastal regions best.",
 "cotton": "👕 Black soil & warm climate with low humidity.",
 "jute": "🧵 Requires warm humid climate & alluvial soil.",
 "coffee": "☕ Prefers cool shade & well-drained soil."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # --- INVALID INPUTS CHECKS ---
        if N < 0 or P < 0 or K < 0:
            flash("❌ N, P, K cannot be negative.", "error")
            return redirect(url_for('index'))

        if N < 5 and P < 5 and K < 5:
            flash("❌ Soil nutrients (N, P, K) too low for any crop to grow.", "error")
            return redirect(url_for('index'))

        if rainfall < 20 or rainfall > 400:
            flash("❌ Rainfall not suitable for any crop (valid 20–400 mm).", "error")
            return redirect(url_for('index'))

        if not (10 <= temperature <= 45):
            flash("❌ Temperature not suitable for crop growth (valid 10–45°C).", "error")
            return redirect(url_for('index'))

        if not (20 <= humidity <= 95):
            flash("❌ Humidity not suitable for crop growth (valid 20–95%).", "error")
            return redirect(url_for('index'))

        if not (4.5 <= ph <= 9.0):
            flash("❌ Soil pH not suitable for crop growth (valid 4.5–9.0).", "error")
            return redirect(url_for('index'))

        # --- Prediction if valid ---
        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        features = mx.transform(features)
        features = sc.transform(features)

        pred = model.predict(features)[0]
        crop_name = inv_crop_dict.get(pred, "Unknown")
        tip = tips.get(crop_name, "No tip available.")

        return render_template("result.html", crop=crop_name, tip=tip)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
