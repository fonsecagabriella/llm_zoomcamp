# --- imports ----------------------------------------------------------
from dotenv import load_dotenv
load_dotenv()  

import os, random
from openai import OpenAI                         # or groq.Client(), etc.
from chat_assistant import Tools, ChatInterface, ChatAssistant



# --- 1️⃣  the actual Python function the agent can call ---------------
def get_weather(city: str):
    # toy stub – replace with real API if you like
    fake_temp = round(random.normalvariate(18, 4), 1)
    return {"city": city, "temperature_c": fake_temp}

# --- 2️⃣  JSON schema that tells the LLM how to call it ---------------
get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Return the current temperature in °C for a given city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "Name of the city to retrieve the weather for."
            }
        },
        "required": ["city"],
        "additionalProperties": False
    }
}

# --- 3️⃣  Wire everything into ChatAssistant --------------------------
tools = Tools()
tools.add_tool(get_weather, get_weather_tool)

developer_prompt = """
You are a polite weather assistant. If the user asks about current weather in
a city, call the get_weather tool; otherwise answer normally.
"""

client = OpenAI()                                 # picks up OPENAI_API_KEY
chat_ui = ChatInterface()

assistant = ChatAssistant(
    tools=tools,
    developer_prompt=developer_prompt,
    chat_interface=chat_ui,
    client=client,
)

assistant.run()       # >>> type questions; 'stop' to exit
