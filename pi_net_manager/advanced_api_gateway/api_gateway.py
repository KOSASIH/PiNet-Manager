# api_gateway.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

app = FastAPI()

# OAuth2 configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Advanced API Gateway with JWT Authentication
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordBearer):
    username = form_data.username
    password = form_data.password
    # Authenticate user and generate JWT token
    token = jwt.encode({"username": username}, "secret_key", algorithm="HS256")
    return JSONResponse(content={"access_token": token}, status_code=200)

# API Endpoints
@app.get("/devices")
async def get_devices(token: str = Depends(oauth2_scheme)):
    # Authenticate token and retrieve devices list
    devices = await get_devices_list(token)
    return JSONResponse(content={"devices": devices}, status_code=200)

@app.post("/devices/{device_id}/commands")
async def send_command(device_id: int, command: str, token: str = Depends(oauth2_scheme)):
    # Authenticate token and send command to device
    await send_command_to_device(device_id, command, token)
    return JSONResponse(content={"message": "Command sent successfully"}, status_code=201)
