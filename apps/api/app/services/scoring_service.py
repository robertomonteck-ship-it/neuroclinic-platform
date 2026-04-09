from sqlalchemy.orm import Session

from app.models.test_response import TestResponse
from app.models.test_result import TestResult


def calculate_test_score(
    db: Session,
    encounter_id: int,
    test_id: int
):

    responses = db.query(
        TestResponse
    ).filter(
        TestResponse.encounter_id == encounter_id
    ).all()

    total_score = 0

    for r in responses:

        try:

            total_score += int(
                r.response_value
            )

        except:

            pass

    classification = classify_score(
        total_score
    )

    interpretation = generate_interpretation(
        classification
    )

    result = TestResult(

        encounter_id=encounter_id,

        test_id=test_id,

        total_score=total_score,

        classification=classification,

        interpretation=interpretation

    )

    db.add(result)

    db.commit()

    db.refresh(result)

    return result


def classify_score(score: int):

    if score <= 10:

        return "mínimo"

    elif score <= 20:

        return "leve"

    elif score <= 30:

        return "moderado"

    else:

        return "grave"


def generate_interpretation(
    classification: str
):

    interpretations = {

        "mínimo":
        "Sem indicativos clínicos relevantes.",

        "leve":
        "Sintomas leves presentes.",

        "moderado":
        "Sintomas moderados requerem atenção clínica.",

        "grave":
        "Sintomas graves indicam necessidade de intervenção."
    }

    return interpretations.get(
        classification,
        "Sem interpretação definida."
    )