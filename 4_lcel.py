from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    chain
)

add_one = lambda x: x+1
double = lambda x: x*2

runnable_add_one = RunnableLambda(add_one)
runnable_double = RunnableLambda(double)

chain = runnable_double | runnable_add_one

print("Chain response:", chain.invoke(4))


llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)

prompt_template = ChatPromptTemplate.from_messages([
    ("system","You are a good summarizer, take the users message and give me a short beautiful comedic summary."),
    ("human","Tell me about {object}")
])

output_parser = StrOutputParser()

summary_chain = prompt_template | llm | output_parser

# print("Summary chain response: ",summary_chain.invoke({"object":"food"}))

summary_old_way = output_parser.invoke(llm.invoke(prompt_template.invoke({"object":"cars"})))

# print("\nSummary old way: ",summary_old_way)




#Runnable parallel

parallel = RunnableParallel(plus_one=runnable_add_one, double=runnable_double)
print("Parallel response:",parallel.invoke(4))

parallel_2 = RunnableParallel(
    chain_1 = runnable_double | runnable_add_one | runnable_double,
    chain_2 = runnable_double | runnable_add_one | runnable_double,
)

print("Parallel response 2:",parallel_2.invoke(4))

summary_parallel = RunnableParallel(
    summary_1 = prompt_template | llm | output_parser
)

print("\n Summary chain response: ",summary_parallel.invoke({"object":"book"}))