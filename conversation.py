from gpt4all import GPT4All
from config import MODEL_PATH

# Initialize GPT4All with a dummy model_name and local path
model = GPT4All(model_name="gpt4all-lora", model_path=MODEL_PATH, allow_download=False)

conversation_history = []

def get_response(user_input):
    conversation_history.append(user_input)
    prompt = "\n".join(conversation_history)
    reply = model.generate(prompt)
    conversation_history.append(reply)
    return reply
