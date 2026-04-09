from app.db.session import SessionLocal
from seed_bdi import seed_bdi_template


def run():

    db = SessionLocal()

    seed_bdi_template(db)

    db.close()


if __name__ == "__main__":
    run()