from app.celery_app import celery_app

@celery_app.task
def process_won_event(event_data):
    # Logic for processing a "won event"
    print(f"Processing won event: {event_data}")
