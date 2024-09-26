from celery import Celery

celery_app = Celery(
    "app",
    broker="pyamqp://guest@localhost//",
    backend="rpc://"
)

celery_app.conf.task_routes = {
    "workers.*": {"queue": "main-queue"},
}
