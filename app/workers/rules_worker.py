from app.celery_app import celery_app

@celery_app.task
def evaluate_rules(rule_data):
    # Processing logic for rule evaluation
    print(f"Evaluating rule: {rule_data}")
