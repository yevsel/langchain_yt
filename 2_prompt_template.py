from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate


llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)


prompt_template = ChatPromptTemplate.from_messages([
    ("system","You are a very funny maths professor who can only answer questions about Calculus."),
    ("human","Tell me about {topic_1} and {topic_2}")
])

response_template = prompt_template.invoke({"topic_1":"Harry Porter","topic_2":"Food"})

print("Template:",response_template.to_messages())

# llm_response = llm.invoke(response_template)

# print("AI Message:",llm_response.content)