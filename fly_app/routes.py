from datetime import timedelta, datetime
from fastapi import APIRouter, Request, status, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from fly_app import app, models, schemas
from fly_app.dependencies import get_db
from fly_app.authourize import decode_token, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import func

fly_router = APIRouter()


#     --   G E T   R E Q U E S T S   --

@app.get("/")
async def get_index():
    return {"message": "Welcome to Fly Jobs API"}





#     --   C R E A T E   R E Q U E S T S   --





#     --   U P D A T E   R E Q U E S T S   --





#     --   D E L E T E   R E Q U E S T S   --