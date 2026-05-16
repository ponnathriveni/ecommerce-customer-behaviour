from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Input schema
class InputData(BaseModel):
    age: float
    salary: float

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/")
def predict(data: InputData):

    try:
        # Convert inputs
        age = float(data.age)
        salary = float(data.salary)

        # Example prediction logic
        prediction = age + salary

        return {
            "prediction": prediction
        }

    except Exception as e:
        return {"error": str(e)}
