from celery import Celery
from celery import shared_task
from core.config import settings
from simulations.simulate import run_simulation

celery_app = Celery(
    __name__,
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)
celery_app.autodiscover_tasks()
celery_app.conf.broker_connection_retry_on_startup = True

@shared_task(name="simulation-queue", bind=True, max_retries=3)
def run_simulation_task(self, count: int = 1000, seed: int = 42):
    try:
        run_simulation(count=count, seed=seed)
        return "Simulation completed successfully."
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
