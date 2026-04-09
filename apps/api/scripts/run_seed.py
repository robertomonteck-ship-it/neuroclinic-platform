from app.core.database import SessionLocal

from scripts.seed_bdi import seed_bdi_template


def run():

    db = SessionLocal()

    try:

        seed_bdi_template(db)

        print("Seed executado com sucesso.")

    except Exception as e:

        print("Erro ao executar seed:")
        print(e)

    finally:

        db.close()


if __name__ == "__main__":
    run()