from app.core.database import engine, Base

# IMPORTANTE: importa todos os models
from app.models import *

def create_tables():

    print("Criando tabelas...")

    Base.metadata.create_all(bind=engine)

    print("Tabelas criadas com sucesso.")


if __name__ == "__main__":
    create_tables()