import random
from datetime import datetime
from sqlalchemy.orm import Session
from models.models import LLM, Metric, SimulationResult
from db.session import SessionLocal

# Seed for reproducibility
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

def generate_metric_value(metric_name: str) -> float:
    if metric_name == "TTFT":
        return round(random.uniform(0.1, 1.0), 3)  # in seconds
    elif metric_name == "TPS":
        return round(random.uniform(10, 1000), 2)  # tokens per second
    elif metric_name == "e2e_latency":
        return round(random.uniform(50, 500), 2)  # in milliseconds
    elif metric_name == "RPS":
        return round(random.uniform(1, 100), 2)  # requests per second
    else:
        return 0.0

def run_simulation(count: int = 1000, seed: int = None):
    if seed is not None:
        random.seed(seed)

    db: Session = SessionLocal()

    llm_names = [
        "GPT-4o",
        "Llama 3.1 405",
        "Mistral Large2",
        "Claude 3.5 Sonnet",
        "Gemini 1.5 Pro",
        "GPT-4o mini",
        "Llama 3.1 70B",
        "amba 1.5Large",
        "Mixtral 8x22B",
        "Gemini 1.5Flash",
        "Claude 3 Haiku",
        "Llama 3.1 8B"
    ]

    metric_names = [
        "TTFT",
        "TPS",
        "e2e_latency",
        "RPS"
    ]

    # Ensure LLMs and Metrics exist
    for name in llm_names:
        llm = db.query(LLM).filter(LLM.name == name).first()
        if not llm:
            llm = LLM(name=name)
            db.add(llm)

    for name in metric_names:
        metric = db.query(Metric).filter(Metric.name == name).first()
        if not metric:
            metric = Metric(name=name)
            db.add(metric)

    db.commit()

    llms = db.query(LLM).all()
    metrics = db.query(Metric).all()

    simulation_results = []
    for llm in llms:
        for metric in metrics:
            for _ in range(count):
                value = generate_metric_value(metric.name)
                simulation = SimulationResult(
                    llm_id=llm.id,
                    metric_id=metric.id,
                    value=value,
                    timestamp=datetime.utcnow()
                )
                simulation_results.append(simulation)

    db.bulk_save_objects(simulation_results, batch_size=1000)
    db.commit()
    db.close()

    print(f"Successfully generated {count * len(llms) * len(metrics)} simulation results.")
