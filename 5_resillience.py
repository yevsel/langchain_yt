from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


primary_model = ChatOpenAI(model="gpt-4o-mini",api_key="wrong-api-key")
backup_model = ChatOllama(model="llama3.1:8b")

# primary_model_response = primary_model.invoke("Hello")


llm = primary_model.with_fallbacks([backup_model])



prompt_template = ChatPromptTemplate.from_messages([
    ("system","You are a very funny maths professor who can only answer questions about Calculus."),
    ("human","Tell me about {topic_1} and {topic_2}")
])

response_template = prompt_template.invoke({"topic_1":"Harry Porter","topic_2":"Food"})

output_parser = StrOutputParser()

chain = (prompt_template | llm | output_parser).with_retry(
    stop_after_attempt=5,
    wait_exponential_jitter=True
)
