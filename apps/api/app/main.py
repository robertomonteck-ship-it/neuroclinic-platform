from fastapi import FastAPI

# Routers existentes (usando nomes reais dos arquivos)

from app.routers.auth_router import router as auth_router
from app.routers.user_router import router as user_router
from app.routers.patient_router import router as patient_router
from app.routers.encounter_router import router as encounter_router
from app.routers.clinical_note_router import router as clinical_note_router
from app.routers.scoring_router import router as scoring_router

from app.routers.test_template import router as test_template_router
from app.routers.test_execution import router as test_execution_router


app = FastAPI(
    title="NeuroClinic API",
    description="Plataforma de Avaliação Neuropsicológica",
    version="1.0.0"
)


# -------------------------
# Registrar routers
# -------------------------

app.include_router(auth_router)

app.include_router(user_router)

app.include_router(patient_router)

app.include_router(encounter_router)

app.include_router(clinical_note_router)

app.include_router(scoring_router)

app.include_router(test_template_router)

# NOVO — execução de testes

app.include_router(test_execution_router)


# -------------------------
# Rota raiz
# -------------------------

@app.get("/")
def root():

    return {
        "message": "NeuroClinic API está funcionando"
    }