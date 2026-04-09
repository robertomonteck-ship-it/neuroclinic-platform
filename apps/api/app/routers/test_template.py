from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal

from app.models.test_template import TestTemplate
from app.models.test_template_question import TestTemplateQuestion
from app.models.test_template_option import TestTemplateOption

from scripts.seed_bdi import seed_bdi_template

router = APIRouter(
    prefix="/templates",
    tags=["Test Templates"]
)


# Dependency DB

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ----------------------------------------
# Listar templates
# ----------------------------------------

@router.get("/")
def list_templates(db: Session = Depends(get_db)):

    templates = db.query(TestTemplate).all()

    return templates


# ----------------------------------------
# Buscar template por código
# ----------------------------------------

@router.get("/{code}")
def get_template(code: str, db: Session = Depends(get_db)):

    template = db.query(TestTemplate).filter(
        TestTemplate.code == code
    ).first()

    if not template:

        return {"error": "Template não encontrado"}

    return template


# ----------------------------------------
# Criar BDI via API
# ----------------------------------------

@router.post("/seed-bdi")
def seed_bdi(db: Session = Depends(get_db)):

    seed_bdi_template(db)

    return {"message": "BDI criado com sucesso"}