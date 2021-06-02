import uvicorn
import pandas as pd
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse, RedirectResponse
from MongoHandler import Mongo_invoices,Mongo_users
from Models import invoices_list,users
# %%init
app = FastAPI()
mongo_invoices = Mongo_invoices()
mongo_users = Mongo_users()

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

@app.get("/invoice/getall")
async def getall():
    out = mongo_invoices.getAll()
    return out.to_dict(orient='records')
@app.post("/invoice/create")
async def create(request:invoices_list):
    rawData = request.dict()["data"]
    # bodyDF = pd.DataFrame(rawData)
    mongo_invoices.insert(rawData)
    return "Successful"



@app.get("/users/getall")
async def getall_user():
    out = mongo_users.getAll()
    return out.to_dict(orient='records')
@app.post("/users/login")
async def login(username:str,password:str):
    # rawData = request.dict()
    # bodyDF = pd.DataFrame(rawData)
    return mongo_users.login(username,password)
    
    # return "Successful"    
@app.get("/users/getbyid")
async def getbyid(member_id:int):
    out = mongo_users.getById(member_id)
    return out.to_dict(orient='records')
@app.post("/users/create")
async def create_user(request:users):
    rawData = request.dict()
    # bodyDF = pd.DataFrame(rawData)
    mongo_users.insert(rawData)
    return "Successful"


# %%Main
if __name__ == '__main__':
    uvicorn.run( app , host='0.0.0.0', port=5000)