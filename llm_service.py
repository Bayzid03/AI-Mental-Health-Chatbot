import os
from dotenv import load_dotenv; load_dotenv()
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    raise ValueError("GROQ API KEY not found")

# HF_TOKEN is used in doc_process.py for document Q&A

llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    api_key=api_key,
    temperature=0
)

session_memory = {}

def get_response(session_id: str, user_query: str) -> str:
    if session_id not in session_memory:
        memory = ConversationBufferMemory()
        session_memory[session_id] = ConversationChain(llm = llm, memory = memory, verbose= True)
    
    conversation = session_memory[session_id]
    return conversation.predict(input=user_query)