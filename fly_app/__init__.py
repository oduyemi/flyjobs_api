from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from .database import SessionLocal
from instance.config import SECRET_KEY, DATABASE_URI

app = FastAPI(title="FlyJob API", description="A job board API that provides endpoints for users to create, read, update, and delete job postings and applicant information. The API also supports authentication using a username and password system.")

engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base: DeclarativeMeta = declarative_base()


from fly_app import routes
app.include_router(routes.fly_router)

