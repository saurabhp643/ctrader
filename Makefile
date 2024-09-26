.PHONY: run
run:
    uvicorn main:app --reload --port 8000

.PHONY: worker
worker:
    celery -A app.celery_app worker --loglevel=info
