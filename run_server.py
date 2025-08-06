import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_environment():
    """Check if required environment variables are set"""
    required_vars = ['GROQ_API_KEY']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
        print("Please create a .env file with the following variables:")
        for var in missing_vars:
            if var == 'GROQ_API_KEY':
                print(f"  {var}=your_groq_api_key_here")
            elif var == 'HF_TOKEN':
                print(f"  {var}=your_huggingface_token_here")
        return False
    
    print("✅ Environment variables loaded successfully")
    return True

if __name__ == "__main__":
    print("🚀 Starting Mental Health ChatBot Server...")
    
    if not check_environment():
        print("❌ Server startup failed due to missing environment variables")
        exit(1)
    
    try:
        print("📡 Beautiful Chat Interface: http://localhost:8000")
        print("📚 API Documentation: http://localhost:8000/docs")
        print("🔧 API Endpoint: http://localhost:8000/api")
        print("⏹️  Press Ctrl+C to stop the server")
        print("-" * 50)
        
        uvicorn.run(
            "main:app",
            host="127.0.0.1",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")
        exit(1) 