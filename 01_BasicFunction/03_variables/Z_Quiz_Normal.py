import random

# List of 50 questions
questions = [
    {"question": "What is the type of 10?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type(10))"},
    {"question": "What is the type of 3.14?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(3.14))"},
    {"question": "What is the type of 'Hello'?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "c", "type_check": "print(type('Hello'))"},
    {"question": "What is the type of True?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "d", "type_check": "print(type(True))"},
    {"question": "What is the type of [1, 2, 3]?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "a", "type_check": "print(type([1, 2, 3]))"},
    {"question": "What is the type of (1, 2, 3)?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "b", "type_check": "print(type((1, 2, 3)))"},
    {"question": "What is the type of {'a': 1, 'b': 2}?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "c", "type_check": "print(type({'a': 1, 'b': 2}))"},
    {"question": "What is the type of {1, 2, 3}?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "d", "type_check": "print(type({1, 2, 3}))"},
    {"question": "What is the type of 0.5?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(0.5))"},
    {"question": "What is the type of 'True'?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "c", "type_check": "print(type('True'))"},
    {"question": "What is the type of 5 + 5.0?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(5 + 5.0))"},
    {"question": "What is the type of None?", "options": ["a) int", "b) float", "c) str", "d) NoneType"], "correct_answer": "d", "type_check": "print(type(None))"},
    {"question": "What is the type of '10'?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "c", "type_check": "print(type('10'))"},
    {"question": "What is the type of {}?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "c", "type_check": "print(type({}))"},
    {"question": "What is the type of {1, 2, 3}?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "d", "type_check": "print(type({1, 2, 3}))"},
    {"question": "What is the type of 10/2?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(10/2))"},
    {"question": "What is the type of '3' + '4'?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "c", "type_check": "print(type('3' + '4'))"},
    {"question": "What is the type of len('Hello')?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type(len('Hello'))"},
    {"question": "What is the type of str(10)?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "c", "type_check": "print(type(str(10)))"},
    {"question": "What is the type of True and False?", "options": ["a) int", "b) float", "c) bool", "d) NoneType"], "correct_answer": "c", "type_check": "print(type(True and False))"},
    # ... Continue with more questions, until there are 50 total
]
questions.extend([
    {"question": "What is the type of 42 + 3.0?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(42 + 3.0))"},
    {"question": "What is the type of {1: 'a', 2: 'b'}?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "c", "type_check": "print(type({1: 'a', 2: 'b'}))"},
    {"question": "What is the type of range(5)?", "options": ["a) list", "b) tuple", "c) dict", "d) range"], "correct_answer": "d", "type_check": "print(type(range(5)))"},
    {"question": "What is the type of open('file.txt', 'r')?", "options": ["a) file", "b) io.TextIOWrapper", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(open('file.txt', 'r'))))"},
    {"question": "What is the type of (1 + 2j)?", "options": ["a) int", "b) float", "c) complex", "d) str"], "correct_answer": "c", "type_check": "print(type(1 + 2j))"},
    {"question": "What is the type of {1, 2, 3} | {2, 3, 4}?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "d", "type_check": "print(type({1, 2, 3} | {2, 3, 4}))"},
    {"question": "What is the type of [1, 2] + [3, 4]?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "a", "type_check": "print(type([1, 2] + [3, 4]))"},
    {"question": "What is the type of 10 // 3?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type(10 // 3))"},
    {"question": "What is the type of [x for x in range(5)]?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "a", "type_check": "print(type([x for x in range(5)]))"},
    {"question": "What is the type of [1, 2, 3] * 2?", "options": ["a) list", "b) tuple", "c) dict", "d) set"], "correct_answer": "a", "type_check": "print(type([1, 2, 3] * 2))"},
    {"question": "What is the type of 'a' * 3?", "options": ["a) str", "b) int", "c) list", "d) bool"], "correct_answer": "a", "type_check": "print(type('a' * 3))"},
    {"question": "What is the type of {'name': 'Alice', 'age': 30}['name']?", "options": ["a) list", "b) tuple", "c) str", "d) dict"], "correct_answer": "c", "type_check": "print(type({'name': 'Alice', 'age': 30}['name']))"},
    {"question": "What is the type of {1: 'a', 2: 'b'}[1]?", "options": ["a) list", "b) tuple", "c) str", "d) dict"], "correct_answer": "c", "type_check": "print(type({1: 'a', 2: 'b'}[1]))"},
    {"question": "What is the type of frozenset([1, 2, 3])?", "options": ["a) set", "b) frozenset", "c) list", "d) tuple"], "correct_answer": "b", "type_check": "print(type(frozenset([1, 2, 3])))"},
    {"question": "What is the type of 2 ** 3?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type(2 ** 3))"},
    {"question": "What is the type of 'abc'.find('b')?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type('abc'.find('b'))"},
    {"question": "What is the type of [1, 2, 3] == [1, 2, 3]?", "options": ["a) bool", "b) int", "c) str", "d) list"], "correct_answer": "a", "type_check": "print(type([1, 2, 3] == [1, 2, 3]))"},
    {"question": "What is the type of [1, 2, 3] != [1, 2, 3]?", "options": ["a) bool", "b) int", "c) str", "d) list"], "correct_answer": "a", "type_check": "print(type([1, 2, 3] != [1, 2, 3]))"},
    {"question": "What is the type of zip([1, 2], ['a', 'b'])?", "options": ["a) list", "b) tuple", "c) dict", "d) zip"], "correct_answer": "d", "type_check": "print(type(zip([1, 2], ['a', 'b'])))"},
    {"question": "What is the type of max([1, 2, 3])?", "options": ["a) int", "b) float", "c) str", "d) list"], "correct_answer": "a", "type_check": "print(type(max([1, 2, 3])))"},
    {"question": "What is the type of round(3.14159, 2)?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "b", "type_check": "print(type(round(3.14159, 2)))"},
    {"question": "What is the type of 'hello'.upper()?", "options": ["a) str", "b) int", "c) list", "d) bool"], "correct_answer": "a", "type_check": "print(type('hello'.upper()))"},
    {"question": "What is the type of isinstance(10, int)?", "options": ["a) bool", "b) int", "c) str", "d) float"], "correct_answer": "a", "type_check": "print(type(isinstance(10, int)))"},
    {"question": "What is the type of ord('A')?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type(ord('A'))"},
    {"question": "What is the type of abs(-10)?", "options": ["a) int", "b) float", "c) str", "d) bool"], "correct_answer": "a", "type_check": "print(type(abs(-10)))"}
])



# Function to run the quiz
def run_quiz():
    score = 0
    num_questions = 10  # We'll ask 10 random questions

    # Shuffle the questions and select 10 random ones
    random.shuffle(questions)
    selected_questions = questions[:num_questions]

    # Loop through the selected questions and ask the user
    for q in selected_questions:
        print(q["type_check"])  # Display the type check print statement
        print(q["question"])
        for option in q["options"]:
            print(option)

        # Get the user's answer
        answer = input("Your answer (a/b/c/d): ").lower()

        # Check if the answer is correct
        if answer == q["correct_answer"]:
            score += 1

    # Calculate and print the result
    percentage = (score / num_questions) * 100
    print(f"\nQuiz complete! You got {score} out of {num_questions} correct.")
    print(f"Your score: {percentage:.2f}%")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
