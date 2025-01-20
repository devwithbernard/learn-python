from typing import List, Dict, Any
from random import shuffle
from requests import get, HTTPError, ConnectionError


def get_possible_answers(question: Dict) -> List[Dict]:
    correct_answer = [question.get('correct_answer')]
    incorrect_answers: List = question.get('incorrect_answers')
    possible_answers: List = incorrect_answers + correct_answer
    shuffle(possible_answers)

    return [{"option": index + 1, "answer": value} for index, value in enumerate(possible_answers)]


def check_response(correct_answer, user_option) -> bool:
    return str(correct_answer).lower() == str(user_option).lower()


def get_data(url) -> List[Dict]:
    try:
        data: Dict[Any] = get(url).json()
        return data.get("results")
    except HTTPError as http_error:
        print(f"Fetching data errors: {http_error.__str__()}")
    except ConnectionError as con_error:
        print(f"Connection to server error: {con_error.__str__()}")
    except Exception as e:
        print(f"Error occurs: {e.__str__()}")
