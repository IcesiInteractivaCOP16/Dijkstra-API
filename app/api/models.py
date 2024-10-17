from pydantic import BaseModel, Field
from typing import List
import heapq

class PathRequest(BaseModel):
    source: str
    destination: str
