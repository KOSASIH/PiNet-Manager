# api_gateway.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2
from fastapi.responses import JSONResponse
from jose import jwt
from pydantic import BaseModel

app = FastAPI()

# OAuth2 configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Advanced API Gateway with JWT Authentication and Role-Based Access Control
class User(BaseModel):
    username: str
    role: str

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordBearer):
    username = form_data.username
    password = form_data.password
    # Authenticate user and generate JWT token with role
    user = await authenticate_user(username, password)
    token = jwt.encode({"username": user.username, "role": user.role}, "secret_key", algorithm="HS256")
    return JSONResponse(content={"access_token": token}, status_code=200)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Authenticate token and retrieve user
    user = await authenticate_token(token)
    return user

# API Endpoints with Role-Based Access Control
@app.get("/devices")
async def get_devices(user: User = Depends(get_current_user)):
    if user.role!= "admin":
        raise HTTPException(status_code=403, detail="Access denied")
    # Retrieve devices list
    devices = await get_devices_list()
    return JSONResponse(content={"devices": devices}, status_code=200)

@app.post("/devices/{device_id}/commands")
async def send_command(device_id: int, command: str, user: User = Depends(get_current_user)):
    if user.role!= "admin":
        raise HTTPException(status_code=403, detail="Access denied")
    # Send command to device
    await send_command_to_device(device_id, command)
    return JSONResponse(content={"message": "Command sent successfully"}, status_code=201)
