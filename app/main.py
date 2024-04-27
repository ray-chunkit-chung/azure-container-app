from contextlib import asynccontextmanager
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import os

######################################################
# Define Application Lifecycle
ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["fake_ml_model"] = fake_ml_model
    ml_models["text_classifier"] = text_classifier
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)

# heroku port setting
PORT = os.environ.get("PORT", 8000)


######################################################
# Input Data Validation
class FakeModelInput(BaseModel):
    IntegerInput: int


class ModelInput(BaseModel):
    IntegerInput: int


######################################################
# Prediction Logic


async def fake_ml_model(data: dict) -> dict:
    prediction = data.get("IntegerInput", 0) * 42
    return {"prediction": prediction}


async def text_classifier(data: dict) -> dict:
    prediction = data.get("IntegerInput", 0) * 42
    return {"prediction": prediction}


######################################################
# Endpoints


@app.get("/")
async def root():
    return {"Nginx": "I'm alive over TvT v9000.46 T.T yametekudastop!!!"}


@app.post("/predict")
async def predict(model_input: ModelInput):
    data = dict(model_input)
    result = await ml_models["text_classifier"](data)
    return {"result": result}


# heroku port setting
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
