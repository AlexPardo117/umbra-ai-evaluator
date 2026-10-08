from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Umbra AI Evaluator API",
    description="API de monitoreo y análisis de calidad de software asistido por IA",
    version="1.0.0"
)

class MetricInput(BaseModel):
    lines_of_code: int = Field(..., gt=0, description="Líneas de código (LOC)")
    defects_found: int = Field(..., ge=0, description="Defectos detectados")

class MetricOutput(BaseModel):
    kloc: float
    defect_density: float
    quality_level: str

@app.get("/", status_code=status.HTTP_200_OK)
def health_check():
    return {
        "status": "Online",
        "service": "Onyx Quality Core",
        "devops_pipeline": "Active"
    }

@app.post("/api/v1/metrics/density", response_model=MetricOutput)
def calculate_defect_density(payload: MetricInput):
    kloc = payload.lines_of_code / 1000.0
    density = payload.defects_found / kloc
    
    if density < 1.0:
        level = "EXCELENTE"
    elif density <= 3.0:
        level = "ACEPTABLE"
    else:
        level = "CRITICO"
        
    return MetricOutput(
        kloc=round(kloc, 3),
        defect_density=round(density, 2),
        quality_level=level
    )