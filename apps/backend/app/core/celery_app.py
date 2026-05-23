from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery_app.conf.task_routes = {
    "app.services.evaluations.run_evaluation": "main-queue"
}

@celery_app.task(acks_late=True)
def run_evaluation_task(evaluation_id: int):
    # This would import the actual evaluation logic
    print(f"Running evaluation {evaluation_id}")
    return {"status": "success", "score": 0.95}
