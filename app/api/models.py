from pydantic import BaseModel, Field
from typing import List

class Coordenada(BaseModel):
    latitud: float = Field(..., description="Latitud de la coordenada")
    altitud: float = Field(..., description="Altitud de la coordenada")

    class Config:
        schema_extra = {
            "example": {
                "latitud": 40.7128,
                "altitud": -74.0060
            }
        }

class Ruta(BaseModel):
    initial: Coordenada
    coordinates: List[Coordenada]
    
    class Config:
        schema_extra = {
            "example": {
                "initial": {
                    "latitud": 40.7128,
                    "altitud": -74.0060
                },
                "coordinates": [
                    {"latitud": 34.0522, "altitud": -118.2437},
                    {"latitud": 51.5074, "altitud": -0.1278}
                ]
            }
        }
