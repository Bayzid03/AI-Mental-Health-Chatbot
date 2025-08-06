import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv; load_dotenv()
from models import ChatRequest
from llm_service import get_response
from crisis import crisis_keyword, SAFETY_MESSAGE
from logger import log_chat
from doc_process import query_doc
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Mental Health ChatBot", version="1.0.0")

# allow cors for frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Mount static files for frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# This route is now handled by serve_frontend()

@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")

@app.get("/api")
def read_root():
    return {"message": "Welcome to the AI Powered Mental Health Chatbot"}

@app.post("/chat")
def chat_with_memory(request: ChatRequest):
    session_id = request.session_id
    user_query = request.query

    if crisis_keyword(user_query):
        log_chat(session_id, user_query, SAFETY_MESSAGE, is_crisis=True)
        return {"response": SAFETY_MESSAGE}

    response = get_response(session_id, user_query)
    log_chat(session_id, user_query, response, is_crisis=False)
    return {"response": response}

@app.post("/doc-chat")
def chat_with_document(request: ChatRequest):
    response = query_doc(request.query)
    return {"response": response}

# Add server startup for direct execution
if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Mental Health ChatBot Server...")
    print("📡 Beautiful Chat Interface: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("🔧 API Endpoint: http://localhost:8000/api")
    print("⏹️  Press Ctrl+C to stop")
    print("-" * 50)
    
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
