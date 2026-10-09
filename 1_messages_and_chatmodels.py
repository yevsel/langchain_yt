from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama


# llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)
# llm = ChatAnthropic(model="claude-haiku-4-5",temperature=0)
llm = ChatOllama(model="llama3.1:8b", temperature=0)

messages = [
    SystemMessage(content="You are a very funny maths professor who can only answer questions about Calculus."),
    HumanMessage(content="Tell me what you know about integration.")
]

llm_response = llm.invoke(messages)


print("AI Message:",llm_response.content,"\n")
print("Model metadata:",llm_response.response_metadata,"\n")
print("IO:",llm_response.usage_metadata,"\n")
print("Response info:",llm_response.id,"\n")

