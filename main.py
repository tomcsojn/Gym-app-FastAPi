import uvicorn
import pandas as pd
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse, RedirectResponse
from MongoHandler import Mongo
from Models import invoices_list
# %%init
app = FastAPI()
mongo = Mongo()

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

@app.get("/getall")
async def getall():
    out = mongo.getAll()
    return out.to_dict(orient='records')
@app.post("/create")
async def create(request:invoices_list):
    rawData = request.dict()["data"]
    bodyDF = pd.DataFrame(rawData)
    mongo.insert(rawData)
    return "Successful"
    


# %%Main
if __name__ == '__main__':
    uvicorn.run( app , host='0.0.0.0', port=5000)