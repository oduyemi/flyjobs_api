from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional, Dict, Union

class JobRequest(BaseModel):
    name: str
    description: str

class JobResponse(BaseModel):
    id: int
    name: str
    description: str