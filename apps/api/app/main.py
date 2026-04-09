from fastapi import FastAPI

from app.core.database import Base, engine

# MODELOS
from app.models.user import User
from app.models.patient import Patient
from app.models.encounter import Encounter
from app.models.clinical_note import ClinicalNote
from app.models.psychological_test import PsychologicalTest
from app.models.test_question import TestQuestion
from app.models.test_response import TestResponse
from app.models.test_result import TestResult

# ROUTERS
from app.routers.user_router import router as user_router
from app.routers.auth_router import router as auth_router
from app.routers.patient_router import router as patient_router
from app.routers.encounter_router import router as encounter_router
from app.routers.clinical_note_router import router as clinical_note_router
from app.routers.scoring_router import router as scoring_router


app = FastAPI(
    title="NeuroClinic API"
)

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(patient_router)
app.include_router(encounter_router)
app.include_router(clinical_note_router)
app.include_router(scoring_router)


@app.get("/")
def read_root():

    return {
        "message": "NeuroClinic API running"
    }


@app.get("/health")
def health():

    return {
        "status": "ok"
    }