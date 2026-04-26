from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import dagshub

# connect to dagshub
dagshub.init(
    repo_owner="nazeebullah",
    repo_name="ShopEase-Sentiment-Analysis",
    mlflow=True
)

# load model from mlflow
model = mlflow.pyfunc.load_model(
    "models:/distilbert-multilingual-sentiment/latest"
)

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(request: TextRequest):
    text = request.text

    prediction = model.predict([text])

    # handle dataframe output safely
    try:
        result = prediction.iloc[0]
        return {
            "input": text,
            "sentiment": str(result["label"]),
            "confidence": float(result["score"])
        }
    except:
        return {
            "input": text,
            "raw_output": str(prediction)
        }