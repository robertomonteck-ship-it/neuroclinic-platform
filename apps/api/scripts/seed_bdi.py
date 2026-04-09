from sqlalchemy.orm import Session

from app.models.test_template import TestTemplate
from app.models.test_template_question import TestTemplateQuestion
from app.models.test_template_option import TestTemplateOption
from app.models.scoring_rules import TestScoringRule


def seed_bdi_template(db: Session):

    print("Criando template BDI...")

    template = TestTemplate(
        name="Beck Depression Inventory II",
        code="BDI-II",
        description="Inventário Beck de Depressão",
        total_questions=21,
        scoring_type="sum"
    )

    db.add(template)
    db.flush()

    # Criar 21 perguntas
    for q_num in range(1, 22):

        question = TestTemplateQuestion(
            template_id=template.id,
            question_number=q_num,
            question_text=f"Question {q_num}"
        )

        db.add(question)
        db.flush()

        # Criar 4 opções por pergunta
        for score in range(4):

            option = TestTemplateOption(
                question_id=question.id,
                option_text=f"Option {score}",
                score_value=score
            )

            db.add(option)

    # Regras clínicas
    rules = [

        (0, 13, "Minimal Depression"),
        (14, 19, "Mild Depression"),
        (20, 28, "Moderate Depression"),
        (29, 63, "Severe Depression")

    ]

    for min_s, max_s, text in rules:

        rule = TestScoringRule(
            template_id=template.id,
            min_score=min_s,
            max_score=max_s,
            interpretation=text
        )

        db.add(rule)

    db.commit()

    print("BDI criado com sucesso.")