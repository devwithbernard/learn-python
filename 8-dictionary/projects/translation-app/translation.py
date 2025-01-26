"""
Translation App
"""

from typing import Dict

translations: Dict[str, ...] = {
    "hello": "bonjour",
    "goodbye": "au revoir",
    "please": "s'il vous plaît",
    "thank you": "merci",
    "yes": "oui",
    "no": "non",
    "how are you?": "comment ça va?",
    "I'm fine": "je vais bien",
    "see you later": "à plus tard",
}


def translate_to_french(word: str) -> str:
    return translations.get(word.lower(), 'Translation not found')


def translate_english(word: str) -> str:
    for key, value in translations.items():
        if value == word.lower():
            return key
    return "Translation not found"


