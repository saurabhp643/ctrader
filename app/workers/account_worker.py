from app.celery_app import celery_app

@celery_app.task
def process_account_creation(account_data):
    # Processing logic for account creation
    print(f"Processing account: {account_data}")
