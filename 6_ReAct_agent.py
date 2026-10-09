# Reason and Act Agent = ReAct Agent

from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
load_dotenv()


#Fake data
ACCOUNTS = {
    "ACC-1001": {"name":"Siril", "pin":"1234", "balance":400.00},
    "ACC-1002": {"name":"Mary", "pin":"9999", "balance": 120.00}
}

def login(account_id: str, pin: str) -> bool:
    """Not a tool, this is to help login"""
    acc = ACCOUNTS.get(account_id)
    if acc and acc["pin"] == pin:
        return True
    return False

@tool
def check_balance(account_id:str) -> dict:
    """Get the current balance of an account"""
    acc = ACCOUNTS.get(account_id)
    if not acc:
        return {"error": "account not found"}
    return {"balance": acc["balance"]}

@tool
def deposit(account_id: str, amount: float) -> dict:
    """Deposit money into an account. Amount must be positive"""
    acc = ACCOUNTS.get(account_id)
    if not acc:
        return {"error": "account not found"}
    if amount <=0:
        return {"error": "amount must be positive"}
    acc["balance"] += amount
    return {"new_balance": acc["balance"]}
    
@tool
def withdraw(account_id:str, amount: float) -> dict:
    """Withdraw money from an account. Amount must be positive and not exceed the balance"""
    acc = ACCOUNTS.get(account_id)
    if not acc:
            return {"error": "account not found"}
    if amount <=0:
        return {"error": "amount must be positive"}
    if amount > acc["balance"]:
        return {"error":"Insufficient funds", "balance": acc["balance"]}
    acc["balance"] -= amount
    return {"new_balance": acc["balance"]}
    


account_id = "ACC-1001"
if not login(account_id=account_id,pin="1234"):
    raise


react_agent = create_agent(
    model=ChatOpenAI(model="gpt-4o-mini", temperature=0),
    tools=[check_balance, deposit, withdraw],
    system_prompt=f"You are a bank assistant. The logged in account is {account_id}. Always use tools for balance and transactions. Never guess an amount."
)

result = react_agent.invoke({
    "messages":[{"role":"user", "content": "Deposit 1000 and then withdraw 500 and tell me my balance"}]
})

print("AI Message:",result["messages"][-1].content)




