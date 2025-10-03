from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained pipeline
with open("pipe.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get screen size & resolution
        screen_size = float(request.form["ScreenSize"])
        resolution = request.form["Resolution"]
        width, height = map(int, resolution.split("x"))
        ppi = ((width**2 + height**2) ** 0.5) / screen_size

        # Prepare features for the pipeline
        input_features = [
            [
                request.form["Company"],
                request.form["TypeName"],
                int(request.form["Ram"]),
                float(request.form["Weight"]),
                int(request.form["Touchscreen"]),
                int(request.form["Ips"]),
                ppi,  # calculated PPI
                request.form["Cpu"],
                int(request.form["HDD"]),
                int(request.form["SSD"]),
                request.form["Gpu"],
                request.form["os"],
            ]
        ]

        # Convert to 2D array
        # input_array = np.array(input_features).reshape(1, -1)

        # Predict using the pipeline
        prediction = model.predict(input_features)[0]
        # prediction = model.predict(input_array)[0]

        return render_template(
            "index.html",
            prediction_text=f"Predicted Laptop Price: ₹ {int(np.exp(prediction))}",
        )

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)
