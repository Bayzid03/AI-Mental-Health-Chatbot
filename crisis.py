from typing import List

CRISIS_KEYWORDS: List[str] = [
    "suicidal", "suicide", "kill myself", "want to die", "hopeless", "worthless", 
    "Can't go on", "give up", "ending at all", "no reason to live"
]

SAFETY_MESSAGE = (
    "It sounds like you're going through a really tough time. "
    "You're not alone, there are people who want to help you. "
    "Please consider reaching out to a mental health professional or contacting a helpline:\n\n"
    "Bangladesh: 234378737537\n"
    "You Matter."
)

def crisis_keyword(text: str) -> bool:
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)



