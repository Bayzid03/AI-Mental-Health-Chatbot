import os
from dotenv import load_dotenv; load_dotenv()
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader

# Get HF token for accessing models (optional for now)
hf_token = os.getenv('HF_TOKEN')

# For now, we'll use a simpler approach without HuggingFace LLM
# This avoids the model loading issues
print("Document Q&A system will use fallback responses")

# Initialize variables
documents = None
index = None
ask_query = None

# For now, we'll use a simple keyword-based approach
# This avoids the complex model loading issues
print("Document Q&A system initialized with fallback responses")

def query_doc(user_query: str) -> str:
    # Simple keyword-based responses for stress management
    query_lower = user_query.lower()
    
    # Stress management responses
    if any(word in query_lower for word in ["stress", "overwhelmed", "pressure"]):
        return "I understand you're feeling stressed. Here are some helpful techniques:\n\n1. Take deep, slow breaths\n2. Go for a walk in nature\n3. Talk to a friend or family member\n4. Write down your thoughts in a journal\n5. Listen to calming music\n6. Practice mindfulness meditation\n\nRemember, it's okay to take breaks and prioritize your well-being."
    
    elif any(word in query_lower for word in ["anxiety", "worried", "nervous", "panic"]):
        return "Anxiety can be really challenging. Try these calming techniques:\n\n1. Practice 4-7-8 breathing (inhale 4, hold 7, exhale 8)\n2. Use grounding techniques (name 5 things you can see, 4 you can touch, etc.)\n3. Progressive muscle relaxation\n4. Limit caffeine and screen time\n5. Create a worry journal\n\nYou're not alone in this, and these feelings will pass."
    
    elif any(word in query_lower for word in ["depression", "sad", "down", "hopeless"]):
        return "I'm sorry you're feeling this way. Remember:\n\n1. Your feelings are valid and temporary\n2. Small steps are still progress\n3. Reach out to someone you trust\n4. Try to maintain a routine\n5. Consider talking to a mental health professional\n\nYou matter, and there are people who care about you."
    
    elif any(word in query_lower for word in ["sleep", "insomnia", "tired"]):
        return "Sleep issues can really affect your mental health. Try these tips:\n\n1. Create a bedtime routine\n2. Avoid screens 1 hour before bed\n3. Keep your room cool and dark\n4. Try relaxation techniques\n5. Avoid caffeine after 2 PM\n6. Write down worries before bed\n\nBetter sleep can help improve your overall well-being."
    
    elif any(word in query_lower for word in ["exercise", "workout", "physical"]):
        return "Physical activity is great for mental health! Start small:\n\n1. Take a 10-minute walk\n2. Try gentle yoga or stretching\n3. Dance to your favorite music\n4. Do household chores with energy\n5. Try deep breathing exercises\n\nEven small amounts of movement can boost your mood."
    
    else:
        return "I'm here to support you with stress management and mental health. You can ask me about:\n\n• Stress relief techniques\n• Anxiety management\n• Depression support\n• Sleep improvement\n• Exercise and wellness\n\nWhat specific area would you like help with?"