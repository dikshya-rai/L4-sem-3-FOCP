import json
import random
import datetime 
import re

# Loading configuration from JSON
def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

def log_conversation(user_input, response):
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"User: {user_input}\nChatbot: {response}\n")

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def chatbot():
    config = load_config()
    agent_name = random.choice(config["agent_names"])
    print(f"Hi! I'm {agent_name}, your virtual assistant.")
    
    user_name = input("What's your name? ").strip()
    print(f"Nice to meet you, {user_name}!")
    
    interaction_count = 0
    while True:
        # Reloading config to allow live updates
        config = load_config()

        user_input = input(f"{user_name}: ").strip().lower()
        
        # Checking for exit commands
        if any(cmd in user_input for cmd in config["exit_commands"]):
            response = random.choice(config["keywords"]["bye"]).format(name=user_name)
            print(f"{agent_name}: {response}")
            log_conversation(user_input, response)
            break
        
        # Keyword matching and responses
        response = None
        for keyword, replies in config["keywords"].items():
            if keyword in user_input:
                if "{time}" in replies[0]:
                    response = random.choice(replies).format(name=user_name, time=get_current_time())
                else:
                    response = random.choice(replies).format(name=user_name)
                break

        if not response:
            response = random.choice(config["default_responses"]).format(name=user_name)
        
        print(f"{agent_name}: {response}")
        log_conversation(user_input, response)

        # Increment interaction count and randomly disconnect
        interaction_count += 1
        if config["random_disconnect"] and interaction_count >= config["max_interactions"]:
            print(f"{agent_name}: Oops, it looks like I need to disconnect. See you later!")
            log_conversation("System", "Random disconnection triggered.")
            break

if __name__ == "__main__": 
    chatbot()  