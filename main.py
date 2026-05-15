from fastapi import FastAPI
import pandas as pd
import pickle

app = FastAPI()


# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Load encoders
encoders = pickle.load(open("encoders.pkl", "rb"))

# Home API
@app.get("/")
def home():
    return {"message": "Ecommerce Customer Behaviour Project Running"}

# Prediction API
@app.post("/predict")
def predict(data: dict):

    input_data = {}

    for key, value in data.items():

        # Encode categorical values
        if key in encoders:
            value = encoders[key].transform([value])[0]

        input_data[key] = [float(value)]

    # Convert input to DataFrame
    df = pd.DataFrame(input_data)

    # Predict
    prediction = model.predict(df)[0]

    if prediction == 1:
        result = "Customer Will Churn"
    else:
        result = "Customer Will Not Churn"

    return {"prediction": result}