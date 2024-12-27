# import os
# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())
# openai_api_key = os.environ["OPENAI_API_KEY"]

# from langchain_openai import OpenAI

# llmModel = OpenAI()


# from langchain_openai import ChatOpenAI

# chatModel = ChatOpenAI(model="gpt-3.5-turbo-0125")

import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain_groq import ChatGroq
#using any model of llama and misteral for testing 
llamaChatModel = ChatGroq(
    model="llama3-70b-8192"
)

mistralChatModel = ChatGroq(
    model="mixtral-8x7b-32768"
)

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.prompts import FewShotChatMessagePromptTemplate

examples = [
    {"input": "hi!", "output": "¡hola!"},
    {"input": "bye!", "output": "¡adiós!"},
]

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an English-Spanish translator."),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)

# chain = final_prompt | chatModel
chain = final_prompt | llamaChatModel

response = chain.invoke({"input": "Who was JFK?"})

print("\n----------\n")

print("Translate: Who was JFK?")
print(response.content)

print("\n----------\n")