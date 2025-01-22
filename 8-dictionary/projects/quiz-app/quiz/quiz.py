from typing import List, Dict, Any
from random import randint


class Quiz:
    questions: list

    def __init__(self, questions: List[Any]):
        self.questions = questions

    def get_random_question(self) -> Dict["str", Any]:
        random_id: int = randint(0, len(self.questions))
        return self.questions[random_id]
