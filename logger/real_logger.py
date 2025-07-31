import os
import time
import random
from openai import OpenAI
from database.models import PromptLog
from database.db_config import SessionLocal
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

# Model pricing (per token)
PRICES = {
    "gpt-4o": 0.000005,
    "gpt-4": 0.00003,
    "gpt-3.5-turbo": 0.0000015,
}

def log_and_call(prompt, model="gpt-4o"):
    start = time.time()

    try:
        if client:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300
            )
            reply = response.choices[0].message.content.strip()
            tokens = response.usage.total_tokens
            model_price = PRICES.get(model, 0.000005)
            cost = round(tokens * model_price, 6)
        else:
            raise Exception("No API key set")

    except Exception as e:
        fake_responses = [
            "Sure, here's a summary...",
            "Quantum computing uses qubits to perform parallel calculations.",
            "The capital of Kazakhstan is Astana.",
            "I'm not sure I understand that. Can you rephrase?"
        ]
        reply = random.choice(fake_responses)
        tokens = random.randint(50, 200)
        cost = round(tokens * 0.00001, 4)
        print(f"[Mocked] Using fallback due to: {e}")

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
