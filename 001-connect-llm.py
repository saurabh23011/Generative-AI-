import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAI


_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]


llmModel = OpenAI()



print("\n----------\n")

response = llamaChatModel.invoke(
    "Tell me one fun fact about the Kennedy family."
)

print("Tell me one fun fact about the Kennedy family:")
print(response)

print("\n----------\n")

print("Streaming:")

for chunk in ChatModel.stream(
    "Tell me one fun fact about the Kennedy family."
):
    print(chunk, end="", flush=True)
    
print("\n----------\n")

creativeLlmModel = OpenAI(temperature=0.9)

response = ChatModel.invoke(
    "Write a short 5 line poem about JFK"
)

print("Write a short 5 line poem about JFK:")
print(response)

print("\n----------\n")

from langchain_openai import ChatOpenAI

chatModel = ChatOpenAI(model="gpt-3.5-turbo-0125")


messages = [
    ("system", "You are an historian expert in the Kennedy family."),
    ("human", "Tell me one curious thing about JFK."),
]
response = ChatModel.invoke(messages)

print("Tell me one curious thing about JFK:")
print(response.content)

print("\n----------\n")

print("Streaming:")

for chunk in ChatModel.stream(messages):
    print(chunk.content, end="", flush=True)
    
print("\n----------\n")