from random import randint
from .models import Pattern


def replace_sign(pattern, pattern_sign, generate_from, generate_to):
    n_patterns = pattern.count(pattern_sign)

    for i in range(n_patterns):
        symbol_index = pattern.find(pattern_sign)
        generated_number = str(randint(generate_from, generate_to))
        pattern = pattern[:symbol_index] + generated_number + pattern[symbol_index + len(pattern_sign):]

    return pattern


def execute_code(pattern):
    def set_execution_result(res):
        global result
        result = res

    pattern = pattern.replace("print", "set_execution_result")
    exec(pattern)

    return result


def compute_pattern(pattern, pattern_sign, generate_from, generate_to):
    '''
    :param pattern: Gets a pattern for execution
    :param pattern_sign: Gets a sign for pattern
    :return: Returns code with numbers without parameters and pattern execution result
    '''

    final_code = replace_sign(pattern, pattern_sign, generate_from, generate_to)
    execution_result = execute_code(final_code)

    return final_code, execution_result


def generate_answers(correct_answer, n_answers, answers_from, answers_to):  # Генерация ответов на вопрос
    answers = [0] * n_answers  # Задается размерность коллекции
    correct_position = randint(0, n_answers - 1)  # Позиция верного ответа

    for i in range(n_answers):  # Перебор всех значений коллекции по их индексу, где i-индекс текущей позиции
        if i == correct_position:  # Если индекс нынешнего элемента совпадает с индексом верного ответа и это значение не входит в ответы
            answers[i] = correct_answer  # Присвоить нынешнему ответу значение верного
        else:
            current_answer = randint(answers_from, answers_to)  # Значение  ответа задать от и до
            while (current_answer in answers) or (current_answer == correct_answer):  # Пока ответ не уникален
                current_answer = randint(answers_from, answers_to)  # Создать новый
            answers[i] = current_answer  # Записать ответ

    return answers


class Question:
    def __init__(self, heading, body, answers, correct_answer):
        self.heading = heading
        self.body = body
        self.answers = answers
        self.correct_answer = correct_answer


def generate_question(topic, difficulty):
    available_patterns = Pattern.objects.filter(topic=topic, difficult=difficulty)
    chosen_pattern = available_patterns[randint(0, len(available_patterns) - 1)]
    text, correct_ans = compute_pattern(chosen_pattern.expression, "$", chosen_pattern.generate_from,
                                        chosen_pattern.generate_to)

    return chosen_pattern, Question(
        heading=chosen_pattern.heading,
        body=text,
        correct_answer=correct_ans,
        answers=generate_answers(correct_ans, 4, chosen_pattern.answer_from, chosen_pattern.answer_to)
    )


def generate_direct_question(topic, difficulty, starting, qc):
    if starting == 1:
        chosen_pattern = Pattern.objects.get(id=23)
    else:
        if qc == 2:
            chosen_pattern = Pattern.objects.get(id=24)
        elif qc == 3:
            chosen_pattern = Pattern.objects.get(id=25)
        elif qc == 4:
            chosen_pattern = Pattern.objects.get(id=26)
        elif qc == 5:
            chosen_pattern = Pattern.objects.get(id=27)
        elif qc == 6:
            chosen_pattern = Pattern.objects.get(id=28)
        elif qc == 7:
            chosen_pattern = Pattern.objects.get(id=29)
        elif qc == 8:
            chosen_pattern = Pattern.objects.get(id=30)
        elif qc == 9:
            chosen_pattern = Pattern.objects.get(id=31)
        elif qc == 10:
            chosen_pattern = Pattern.objects.get(id=32)
        elif qc == 11:
            chosen_pattern = Pattern.objects.get(id=33)
        elif qc == 12:
            chosen_pattern = Pattern.objects.get(id=34)
        elif qc == 13:
            chosen_pattern = Pattern.objects.get(id=35)
        elif qc == 14:
            chosen_pattern = Pattern.objects.get(id=36)
        elif qc == 15:
            chosen_pattern = Pattern.objects.get(id=37)
        elif qc == 16:
            chosen_pattern = Pattern.objects.get(id=38)
        elif qc == 17:
            chosen_pattern = Pattern.objects.get(id=39)
        elif qc == 18:
            chosen_pattern = Pattern.objects.get(id=40)
        elif qc == 19:
            chosen_pattern = Pattern.objects.get(id=41)
        elif qc == 20:
            chosen_pattern = Pattern.objects.get(id=42)

    text, correct_ans = compute_pattern(chosen_pattern.expression, "$", chosen_pattern.generate_from,
                                        chosen_pattern.generate_to)

    return chosen_pattern, Question(
        heading=chosen_pattern.heading,
        body=text,
        correct_answer=correct_ans,
        answers=generate_answers(correct_ans, 4, chosen_pattern.answer_from, chosen_pattern.answer_to)
    )

