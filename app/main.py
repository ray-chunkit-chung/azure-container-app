from fastapi import FastAPI
import os

app = FastAPI()

# heroku port setting
PORT = os.environ.get('PORT', 8000)


@app.get("/")
async def root():
    return {"Nginx": "I'm alive over TvT v9000 T.T yametekudastop!!!"}

# heroku port setting
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
