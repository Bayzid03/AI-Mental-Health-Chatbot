# Mental Health Support ChatBot

A compassionate AI-powered mental health support chatbot designed to provide emotional support, crisis intervention, and stress management guidance.

## Demo



## 🌟 Features

### Core Functionality
- **Conversational AI**: Powered by Groq API for natural, empathetic conversations
- **Crisis Detection**: Automatically detects suicidal thoughts and provides immediate help
- **Memory System**: Maintains conversation context for personalized support
- **Document Q&A**: Access to stress management tips and mental health resources
- **Session Management**: Unique session tracking for each user

### Mental Health Features
- **Crisis Intervention**: Immediate safety messages and helpline information
- **Stress Management**: Access to 100+ stress relief techniques
- **Emotional Support**: Compassionate responses to mental health concerns
- **Safety First**: Built-in crisis detection with appropriate interventions

### User Interface
- **Beautiful Design**: Modern, calming interface with gradient backgrounds
- **Dark/Light Theme**: Toggle between themes for user comfort
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Accessibility**: Screen reader friendly and keyboard navigation
- **Quick Actions**: Pre-defined buttons for common mental health topics

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- GROQ API key (get it from [Groq Console](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Mental-Health-ChatBot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   HF_TOKEN=your_huggingface_token_here  # Optional
   ```

4. **Run the backend server**
   
   **Option 1 (Recommended):**
   ```bash
   python run_server.py
   ```
   
   **Option 2 (Direct):**
   ```bash
   python main.py
   ```
   
       **Option 3 (Manual uvicorn):**
    ```bash
    uvicorn main:app --reload --host 127.0.0.1 --port 8000
    ```

5. **Open the application**
   - Visit `http://localhost:8000` in your browser for the beautiful chat interface
   - Everything is integrated - no separate links needed!

## 📁 Project Structure

```
Mental Health ChatBot/
├── main.py              # FastAPI backend server
├── models.py            # Pydantic data models
├── llm_service.py       # Groq AI integration
├── crisis.py            # Crisis detection and safety messages
├── logger.py            # Chat logging system
├── doc_process.py       # Document Q&A with keyword-based responses
├── data/
│   └── stress_management.txt  # Stress relief techniques
├── frontend/
│   ├── index.html       # Beautiful chat interface
│   └── design.css       # Modern, mental health-friendly styling
└── requirements.txt     # Python dependencies
```

## 🔧 API Endpoints

### `/` (GET)
- Welcome message for the API

### `/chat` (POST)
- Main conversation endpoint
- Requires: `session_id`, `query`
- Returns: AI response with crisis detection

### `/doc-chat` (POST)
- Document-based Q&A
- Requires: `session_id`, `query`
- Returns: Information from stress management data

## 🎨 Frontend Features

### Design Philosophy
- **Calming Colors**: Soft gradients and soothing color palette
- **Smooth Animations**: Gentle transitions and loading indicators
- **Mental Health Friendly**: Non-triggering design elements
- **Accessibility**: High contrast, keyboard navigation, screen reader support

### Key Components
- **Welcome Message**: Compassionate introduction
- **Real-time Chat**: Smooth message flow with timestamps
- **Quick Actions**: Pre-defined mental health topics
- **Crisis Modal**: Emergency contact information
- **Theme Toggle**: Dark/light mode for user comfort
- **Character Counter**: Prevents overwhelming messages
- **Loading States**: Gentle feedback during AI processing

## 🛡️ Safety Features

### Crisis Detection
The chatbot automatically detects keywords related to:
- Suicidal thoughts
- Self-harm
- Hopelessness
- Worthlessness

### Safety Response
When crisis keywords are detected:
1. Immediate safety message
2. Crisis modal with helpline information
3. Emergency contact numbers
4. Compassionate support message

### Helpline Information
- **Bangladesh Crisis Helpline**: 234378737537
- **Emergency Services**: 999

## 🔒 Privacy & Security

- **Session-based**: Each conversation is isolated
- **No Data Storage**: Messages are not permanently stored
- **Local Processing**: Document Q&A runs locally
- **Secure API**: HTTPS communication with Groq

## 🎯 Mental Health Best Practices

### Design Considerations
- **Non-triggering**: Avoid potentially harmful content
- **Compassionate**: Warm, supportive language
- **Accessible**: Easy to use for people with various needs
- **Responsive**: Adapts to user's emotional state

### Crisis Intervention
- **Immediate Response**: Quick detection and response
- **Clear Information**: Easy-to-find helpline numbers
- **Compassionate Approach**: Non-judgmental support
- **Professional Guidance**: Encourages professional help

## 🚀 Deployment

### Local Development
```bash
# Backend
python main.py

# Frontend (in another terminal)
cd frontend
python -m http.server 8080
```

### Production Deployment
1. Set up a production server
2. Configure environment variables
3. Use a proper web server (nginx, Apache)
4. Set up SSL certificates
5. Configure CORS properly

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Important Disclaimer

This chatbot is designed to provide emotional support and information, but it is **NOT a substitute for professional mental health care**. 

**If you're experiencing a mental health crisis:**
- Contact a mental health professional
- Call your local crisis helpline
- Go to the nearest emergency room
- You are not alone, and help is available

## 🆘 Emergency Resources

- **National Suicide Prevention Lifeline**: 988 (US)
- **Crisis Text Line**: Text HOME to 741741 (US)
- **Emergency Services**: 911 (US) / 999 (UK) / 112 (EU)
- **Local Mental Health Services**: Contact your healthcare provider

---

**Remember**: You matter, and your mental health is important. Reach out for help when you need it. 💙 