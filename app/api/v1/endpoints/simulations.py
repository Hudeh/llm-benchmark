from fastapi import APIRouter
from tasks.celery_tasks import run_simulation_task

router = APIRouter()

@router.post("/run-simulation/")
async def run_simulation(count: int = 1000, seed: int = 42):
    """
    API endpoint to trigger Celery task for running simulations.

    Args:
        count (int): Number of simulations to run. Default is 1000.
        seed (int): Seed value for random number generation. Default is 42.

    Returns:
        dict: Celery task ID for tracking.
    """
    task = run_simulation_task.delay(count, seed)
    return {"task_id": task.id, "status": "Task submitted successfully."}

@router.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    """
    API endpoint to check the status of the Celery task.

    Args:
        task_id (str): The task ID of the Celery job.

    Returns:
        dict: Task status, result (if completed), or error (if failed).
    """
    task = run_simulation_task.AsyncResult(task_id)
    return {"task_id": task_id, "status": task.status, "result": task.result}
