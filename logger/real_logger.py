import random
import time
from database.db_config import SessionLocal
from database.models import PromptLog

def log_and_call(prompt, model="gpt-4o"):
    start = time.time()

    # Mocked response
    fake_responses = [
        "Sure, here's a summary...",
        "Quantum computing uses qubits to perform parallel calculations.",
        "The capital of France is Paris.",
        "I'm not sure I understand that. Can you rephrase?"
    ]
    reply = random.choice(fake_responses)
    tokens = random.randint(50, 200)
    cost = round(tokens * 0.00001, 4)
    latency = round((time.time() - start) * 1000)

    db = SessionLocal()
    log = PromptLog(
        prompt=prompt,
        response=reply,
        model=model,
        tokens=tokens,
        cost=cost,
        latency_ms=latency
    )
    db.add(log)
    db.commit()
    db.close()

    return reply
