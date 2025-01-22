from quiz.quiz import Quiz
from quiz.utils import check_response, get_data, get_possible_answers
from typing import List, Dict


def main() -> None:
    questions: List[Dict] = get_data("https://opentdb.com/api.php?amount=10")
    quiz: Quiz = Quiz(questions)

    score: int = 0

    while True:
        question: Dict = quiz.get_random_question()
        possible_answers: List = get_possible_answers(question)

        print(f"{question['question']}")
        print("Responses: ")
        for possible_answer in possible_answers:
            print(f"\t{possible_answer['option']} => {possible_answer['answer']}")
        try:
            user_option: int = int(input("Choose the correct response:"))

            if check_response(question['correct_answer'], possible_answers[user_option - 1]):
                score += 10
                print("Super!!!")
            else:
                print("Wrong response")

            if score == 20:
                break
        except ValueError as v_error:
            print("Problème de choix de réponse!")
        except IndexError as index_error:
            print("Choix hors des valeurs autorisées!")

    print(f"Score final: {score} pts")


if __name__ == '__main__':
    main()
