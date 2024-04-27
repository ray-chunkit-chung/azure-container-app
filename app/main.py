from contextlib import asynccontextmanager
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import os


# Input Data Validation
class ModelInput(BaseModel):
    IntegerInput: int


async def fake_ml_model(data: dict) -> dict:
    prediction = data.get("IntegerInput", 0) * 42
    return {"prediction": prediction}


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["fake_ml_model"] = fake_ml_model
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)

# heroku port setting
PORT = os.environ.get("PORT", 8000)


@app.get("/")
async def root():
    return {"Nginx": "I'm alive over TvT v9000.48 T.T yametekudastop!!!"}


@app.post("/predict")
async def predict(model_input: ModelInput):
    data = dict(model_input)
    result = await ml_models["fake_ml_model"](data)
    return {"result": result}


# heroku port setting
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
