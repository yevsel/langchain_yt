from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class Footballer(BaseModel):
    name: str = Field(description="Name of the footballer")
    club_team: str = Field(description="This is the the club team the footballer plays for")
    nationality: str = Field(description="The country of origin")
    

structured_llm = ChatOpenAI(model="gpt-4o-mini",temperature=0).with_structured_output(Footballer)

llm_response = structured_llm.invoke("Give me the information of 1 random footballer from USA")

print("AI Message:",llm_response)
print("Name:",llm_response.name)
print("Club team:",llm_response.club_team)
print("Nationality:",llm_response.nationality)