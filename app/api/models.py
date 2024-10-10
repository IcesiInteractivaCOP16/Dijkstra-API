from pydantic import BaseModel, Field
from typing import List
import heapq

class Coordenada(BaseModel):
    latitud: float = Field(..., description="Latitud de la coordenada")
    longitud: float = Field(..., description="Longitud de la coordenada")
    adyacentes: List['Coordenada'] = Field(default_factory=list, description="Lista de coordenadas adyacentes")
   
    def __hash__(self):
        return hash((self.latitud, self.longitud))
    
    def __eq__(self, other):
        if isinstance(other, Coordenada):
            return self.latitud == other.latitud and self.longitud == other.longitud
        return False

    class Config:
        schema_extra = {
            "example": {
                "initial": {
                    "latitud": 40.7128,
                    "longitud": -74.0060,
                    "adyacentes": []
                },
                "coordinates": [
                    {
                        "latitud": 34.0522,
                        "longitud": -118.2437,
                        "adyacentes": []
                    },
                    {
                        "latitud": 41.8781,
                        "longitud": -87.6298,
                        "adyacentes": []
                    }
                ],
                "final": {
                    "latitud": 37.7749,
                    "longitud": -122.4194,
                    "adyacentes": []
                }
            }
        }

class Ruta(BaseModel):
    initial: Coordenada
    coordinates: List[Coordenada]
    final: Coordenada
    
    class Config:
        schema_extra = {
            "example": {
                "initial": {
                    "latitud": 40.7128,
                    "longitud": -74.0060
                },
                "coordinates": [
                    {"latitud": 34.0522, "altitud": -118.2437},
                    {"longitud": 51.5074, "altitud": -0.1278}
                ],
                "final": {
                    "latitud": 48.8566,
                    "longitud": 2.3522
                }
            }
        }
