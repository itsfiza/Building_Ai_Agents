import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
#creating a client
client=Groq(
    api_key = os.getenv("GROQ_API_KEY")
)
messages =[]
while True:
    question = input("You: ")
    messages.append(
    {
        "role":"user",
        "content":question
    }
)
# send msgf to LLM
    response=client.chat.completions.create(
        model= "llama-3.3-70b-versatile",
        messages=messages
    )
    bot_reply = response.choices[0].message.content
    messages.append(
    {
        "role":"assistant",
        "content":bot_reply
    }
)
    print("Bot: ",bot_reply)
