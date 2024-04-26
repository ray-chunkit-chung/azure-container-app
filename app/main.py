from contextlib import asynccontextmanager
from fastapi import FastAPI
import os


async def fake_answer_to_everything_ml_model(x: int):
    return x * 42


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)

# heroku port setting
PORT = os.environ.get("PORT", 8000)


@app.get("/")
async def root():
    return {"Nginx": "I'm alive over TvT v9000.49 T.T yametekudastop!!!"}


@app.post("/predict")
async def predict(x: int):
    result = ml_models["answer_to_everything"](x)
    return {"result": result}


# heroku port setting
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
