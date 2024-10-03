from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define the FastAPI app
app = FastAPI()

# Define the input data schema
class Input(BaseModel):
    test_preparation_course: int
    math_score: int
    reading_score: int
    writing_score: int

# Define the prediction endpoint
@app.post("/predict")
def predict(input_data: Input):
    data = [[
        input_data.test_preparation_course,
        input_data.math_score,
        input_data.reading_score,
        input_data.writing_score
    ]]
    
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
