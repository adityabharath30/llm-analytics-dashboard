from logger.real_logger import log_and_call

# List of example prompts
prompts = [
    "Explain quantum computing in one sentence.",
    "What are the key differences between Python and Java?",
    "Summarize the plot of Inception in 3 lines.",
    "Translate 'Good morning, how are you?' to French.",
    "Write a short poem about the ocean.",
    "What are the benefits of regular exercise?",
    "Who was Ada Lovelace and why is she important?",
    "Give me 3 dinner ideas using only eggs and potatoes.",
    "Draft an email to request a meeting with my manager.",
    "What is the capital of Kazakhstan?",
]

for prompt in prompts:
    reply = log_and_call(prompt)
    print(f"Prompt: {prompt}\nResponse: {reply}\n{'-'*40}")
