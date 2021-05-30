import uvicorn
import pandas as pd
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse, RedirectResponse
# %%init
app = FastAPI()

# %%Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/")
async def default():
    response = RedirectResponse(url='/docs')
    return response

# %%Main
if __name__ == '__main__':
    uvicorn.run( app , host='0.0.0.0', port=5000)