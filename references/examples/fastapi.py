from fastapi import FastAPI
from obs_metrics import FastApiMiddleware

app = FastAPI()
app.add_middleware(FastApiMiddleware)

@app.get("/ping")
async def ping():
    return {"message": "pong"}